// Task3: This script adds the class red to the <header> element when
// the user clicks on the tag DIV#red_header
$('#red_header').click(function() {
  const headerElement = $('header');
  headerElement.addClass('red');
});
