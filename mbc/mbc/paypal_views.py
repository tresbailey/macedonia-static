import braintree

from decimal import Decimal
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView
from mezzanine.conf import settings
from mezzanine.utils.views import render, set_cookie, paginate
from paypal_forms import TokenForm

TWOPLACES = Decimal(10) ** -2 
SERVICE_PERCENT = 1.03

def client_token(request, template="dropin.html", form_class=TokenForm, extra_content=None):
    if 'clientToken' not in request.session:
        braintree.Configuration.configure(settings.BRAINTREE_ENVIRONMENT,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY)

        token = braintree.ClientToken.generate()
        request.session['clientToken'] = token
    response = render(request, template, extra_content)
    return response


def save_nonce(request):
    nonce = request._post['payment_method_nonce']
    request.session['payment_nonce'] = nonce
    return JsonResponse({'nonce': nonce})



def send_payment(request, template="paid.html", form_class=TokenForm, extra_content=None):
    if 'POST' == request.method:
        braintree.Configuration.configure(settings.BRAINTREE_ENVIRONMENT,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY)
        nonce = request.session['payment_nonce']
        total_charge = Decimal(request._post['tithe_amount']) * Decimal(SERVICE_PERCENT)
        total_charge = str(total_charge.quantize(TWOPLACES))
        result = braintree.Transaction.sale({
            "amount": total_charge,
            "payment_method_nonce": nonce
        })
        extra_content  = {'amount': total_charge, 'giver': request._post['giver']}
    return render(request, template, extra_content)

