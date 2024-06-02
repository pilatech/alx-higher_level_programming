$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, code) {
    if (code === 'success') {
      for (const movie of data.results) {
        $('ul#list_movies').append(`<li>${movie.title}</li>`);
      }
    }
  });
});
