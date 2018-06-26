$('DIV#toggle_header').click(function () {
  if ($('header').attr('class') === 'green') {
    $('header').attr('class', 'red');
  } else {
    $('header').attr('class', 'green');
  }
});
