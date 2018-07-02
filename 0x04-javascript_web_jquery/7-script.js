window.onload = function () {
  let theURL = 'https://swapi.co/api/people/5/?format=json';
  $.ajax({
    url: theURL,
    success: function (res) {
      $('DIV#character').text(res.name);
    },
    error: function (err) {
      console.log(err);
    }
  });
};
