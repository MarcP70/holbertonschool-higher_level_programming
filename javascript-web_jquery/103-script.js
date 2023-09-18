$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();

    // Check if the language code is provided
    if (languageCode) {
      // Make an AJAX request to fetch the translation
      $.ajax({
        url: `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`,
        type: 'GET',
        success: function (data) {
          // Update the content of the <div> with the translation
          $('#hello').text(data.hello);
        },
        error: function (error) {
          console.log('Error fetching translation:', error);
        }
      });
    }
  }

  // Trigger translation when the Translate button is clicked
  $('#btn_translate').click(fetchTranslation);

  // Trigger translation when ENTER is pressed in the language code input
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      // ENTER key code
      fetchTranslation();
    }
  });
});
