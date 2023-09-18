// Task12: This script  fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $('#btn_translate').click(function () {
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
  });
});
