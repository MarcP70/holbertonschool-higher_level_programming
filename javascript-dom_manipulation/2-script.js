// 2-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the element with the id "red_header"
  var redHeaderElement = document.getElementById('red_header');

  // Add a click event listener to the selected element
  redHeaderElement.addEventListener('click', function () {
    // Select the header element
    var headerElement = document.querySelector('header');

    // Add the "red" class to the header element
    headerElement.classList.add('red');
  });
});
