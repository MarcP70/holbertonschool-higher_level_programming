// 8-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the element with the id "hello"
  var helloElement = document.getElementById('hello');

  // Fetch the translation of "hello" from the URL
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
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
      // Extract the translation of "hello" from the JSON data
      var helloTranslation = data.hello;
      
      // Update the text content of the "hello" element with the translation
      helloElement.textContent = helloTranslation;
    })
    .catch(function (error) {
      console.error(error);
    });
});
