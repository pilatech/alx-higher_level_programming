$(function () {
  $('div#toggle_header').bind('click', function () {
    const header = $('header');
    if (header.hasClass('green')) {
      header.removeClass('green');
      header.addClass('red');
    } else {
      header.removeClass('red');
      header.addClass('green');
    }
  });
});
