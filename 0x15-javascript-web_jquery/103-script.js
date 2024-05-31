$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) { // 13 is the keycode for ENTER
      fetchTranslation();
    }
  });
});
