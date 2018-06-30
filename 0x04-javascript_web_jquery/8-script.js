$.ajax({
  url: 'https://swapi.co/api/films?format=json',
  success: function (res) {
    res.results.map(function (elem) {
      const item = document.createElement('li');
      $(item).text(elem.title);
      $('UL#list_movies').append(item);
    });
  }
});
