$(function () {
  $('input#btn_translate').bind('click', function () {
    const lan = $('input#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lan}`, function (data, sCode) {
      if (sCode === 'success') {
        $('div#hello').text(data.hello);
      }
    });
  });
});
