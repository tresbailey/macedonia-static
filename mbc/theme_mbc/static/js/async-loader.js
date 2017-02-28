$(document).ready(function() {
  $('input[name="childSlug"]').each(function(index, ele) {
    console.log($(ele).val());
    $.ajax($(ele).val(), {async: true}).done(function( data ) {
      // Why is it not ending divs properly?
      $('.page-specific .asyncSlug:eq('+index+')').append(data);
    });
  });
});

