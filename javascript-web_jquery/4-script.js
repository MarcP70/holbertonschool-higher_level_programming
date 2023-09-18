// Task4: This script toggles the class of the <header> element when
// the user clicks on the tag DIV#toggle_header
$(document).ready(function() {
  // Attach a click event to the div with ID toggle_header
  $('#toggle_header').click(function() {
    const headerElement = $('header');

    // Toggle the 'red' and 'green' classes on the header
    headerElement.toggleClass('red green');
  });
});
