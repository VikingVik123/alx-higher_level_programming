$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
