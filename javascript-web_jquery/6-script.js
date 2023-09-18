// Task 6: This script updates the text of the <header> element to New Header!!!
// when the user clicks on DIV#update_header
$(document).ready(function () {
  // Attach a click event to the div with ID update_header
  $('#update_header').click(function () {
    // Select the <header> element and update its text content
    $('header').text('New Header!!!');
  });
});
