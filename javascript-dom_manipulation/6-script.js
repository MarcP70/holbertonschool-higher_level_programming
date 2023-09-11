// 6-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the element with the id "character"
  var characterElement = document.getElementById('character');

  // Fetch the character data from the URL
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(function (response) {
      // Check if the response is successful (status code 200)
      if (response.status === 200) {
        // Parse the response JSON
        return response.json();
      } else {
        throw new Error('Failed to fetch character data');
      }
    })
    .then(function (data) {
      // Extract the character name from the data
      var characterName = data.name;

      // Update the text content of the characterElement with the character name
      characterElement.textContent = characterName;
    })
    .catch(function (error) {
      console.error(error);
    });
});
