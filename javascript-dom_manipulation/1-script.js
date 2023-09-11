// 1-script.js
// This script updates the text color of the header element to red (#FF0000)
// when the user clicks on the tag with id red_header.
document.addEventListener('DOMContentLoaded', function () {
  // Select the element with the id "red_header"
  var redHeaderElement = document.getElementById('red_header');

  // Add a click event listener to the selected element
  redHeaderElement.addEventListener('click', function () {
    // Select the header element
    var headerElement = document.querySelector('header');

    // Update the text color to red (#FF0000)
    headerElement.style.color = '#FF0000';
  });
});
