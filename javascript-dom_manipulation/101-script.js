// 101-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the elements with ids "language_code" and "btn_translate"
  var languageCodeElement = document.getElementById('language_code');
  var translateButtonElement = document.getElementById('btn_translate');
  
  // Select the element with id "hello" to display the translation
  var helloElement = document.getElementById('hello');

  // Function to fetch and display the translation
  function fetchAndDisplayTranslation() {
    // Get the selected language code from the combo box
    var selectedLanguage = languageCodeElement.value;

    // Check if a language is selected
    if (selectedLanguage) {
      // Construct the API URL with the selected language code
      var apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=' + selectedLanguage;

      // Fetch the translation data from the API
      fetch(apiUrl)
        .then(function (response) {
          // Check if the response is successful (status code 200)
          if (response.status === 200) {
            // Parse the response text as JSON
            return response.json();
          } else {
            throw new Error('Failed to fetch translation data');
          }
        })
        .then(function (data) {
          // Extract the translation of "Hello" from the JSON data
          var helloTranslation = data.hello;
          
          // Update the text content of the "hello" element with the translation
          helloElement.textContent = helloTranslation;
        })
        .catch(function (error) {
          console.error(error);
        });
    }
  }

  // Add a click event listener to the "Translate" button
  translateButtonElement.addEventListener('click', fetchAndDisplayTranslation);
});
