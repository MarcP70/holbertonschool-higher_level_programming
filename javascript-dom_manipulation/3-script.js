// 3-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the element with the id "toggle_header"
  var toggleHeaderElement = document.getElementById('toggle_header');

  // Add a click event listener to the selected element
  toggleHeaderElement.addEventListener('click', function () {
    // Select the header element
    var headerElement = document.querySelector('header');

    // Check if the current class is "red" or "green" and toggle it accordingly
    if (headerElement.classList.contains('red')) {
      headerElement.classList.remove('red');
      headerElement.classList.add('green');
    } else {
      headerElement.classList.remove('green');
      headerElement.classList.add('red');
    }
  });
});
