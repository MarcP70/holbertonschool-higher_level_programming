// 5-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the element with the id "update_header"
  var updateHeaderElement = document.getElementById('update_header');

  // Add a click event listener to the selected element
  updateHeaderElement.addEventListener('click', function () {
    // Select the header element
    var headerElement = document.querySelector('header');

    // Update the text content of the header element
    headerElement.textContent = 'New Header!!!';
  });
});
