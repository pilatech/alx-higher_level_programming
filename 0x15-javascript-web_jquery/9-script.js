$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, code) {
    if (code === 'success') {
      $('div#hello').text(data.hello);
    }
  });
});
