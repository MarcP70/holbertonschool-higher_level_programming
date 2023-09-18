// Task9: this script fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello
$(document).ready(function () {
  // URL to fetch the translation of "hello"
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Make an AJAX request to fetch the translation
  $.ajax({
    url: apiUrl,
    type: 'GET',
    success: function (data) {
      // Update the content of the <div> with the translation
      $('#hello').text(data.hello);
    },
    error: function (error) {
      console.log('Error fetching translation:', error);
    }
  });
});
