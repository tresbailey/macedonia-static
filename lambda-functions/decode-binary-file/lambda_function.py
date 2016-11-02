from __future__ import print_function

import json
import urllib
import boto3
import base64
import os
import requests

import StringIO

print('Iam Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get the object from the event and show its content type
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        body = response['Body'].read()
        decoded = StringIO.StringIO(base64.b64decode(body))
        s3.put_object(
            Bucket=bucket, 
            Key='%s/%s' % (os.path.dirname(key), os.path.basename(key).rstrip('.b64')),
            Body=decoded,
            ContentType='application/pdf')
        decoded.seek(0)
        s3.put_object(
            Bucket=bucket, 
            Key=os.path.dirname(key) +'/latest.pdf',
            Body=decoded,
            ContentType='application/pdf')
        decoded.seek(0)
        s3.delete_object(Bucket=bucket, Key=key)
        
        
        requests.post(
        "https://api.mailgun.net/v3/macedoniaofgaffney.com/messages",
        auth=("api", "key-43c6c3d0cc532cf009ad7e90861352a4"),
        files={"attachment": ('newsletter.pdf', decoded, 'application/pdf')},
        data={"from": "Excited User <mailgun@macedoniaofgaffney.com>",
              "to": ["admin@macedoniaofgaffney.com"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

