$(document).ready(function() {
  $('input[name="childSlug"]').each(function(index, ele) {
    console.log($(ele).val());
    $.ajax($(ele).val(), {async: true}).done(function( data ) {
      console.log(data);
      $('.page-specific').append(data);
    });
  });
});

