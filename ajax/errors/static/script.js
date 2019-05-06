function clearErrors() {
  $('.error').remove()
}

$(document).ready(function() {
  $('#reg-form').submit(function(event) {
    event.preventDefault();
    $.ajax({
      url: '/process',
      method: 'POST',
      data: $('#reg-form').serialize(),
      success: function(data) {
        clearErrors()
        $('body').append(data.message)
      },
      error: function(err) {
        clearErrors()
        for(let key in err.responseJSON) {
          $(`#${key}`).after(`<p class="error">${err.responseJSON[key]}</p>`);
        }
      }
    });
  });
});