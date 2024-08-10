$(document).ready(function () {
  $('INPUT#btn_translate').click(handleLang);
  $('INPUT#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      handleLang();
    }
  });

  function handleLang () {
    const lan = $('INPUT#language_code').val();
    $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lan}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
});
