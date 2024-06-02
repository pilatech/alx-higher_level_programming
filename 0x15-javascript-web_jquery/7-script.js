$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, code) {
    if (code === 'success') {
      $('div#character').text(data.name);
    }
  });
});
