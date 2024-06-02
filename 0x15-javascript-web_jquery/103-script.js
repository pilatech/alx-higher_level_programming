$(function () {
  $('input#language_code').bind('keyup', function (evt) {
    if (evt.key === 'Enter' || evt.keyCode === 13) {
      getData();
    }
  });

  $('input#btn_translate').bind('click', getData);

  function getData () {
    const lan = $('input#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lan}`, function (data, sCode) {
      if (sCode === 'success') {
        $('div#hello').text(data.hello);
      }
    });
  }
});
