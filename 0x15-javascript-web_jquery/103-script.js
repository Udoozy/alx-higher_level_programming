$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (i) {
      if (i.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(apiUrl + $.param({ lang: $('INPUT#language_code').val() }), function (output) {
    $('DIV#hello').html(output.hello);
  });
}
