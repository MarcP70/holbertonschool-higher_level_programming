// Task5: This script adds a <li> element to a list when the user clicks
// on the tag DIV#add_item
$(document).ready(function () {
  // Attach a click event to the div with ID add_item
  $('#add_item').click(function () {
    // Create a new <li> element with the specified content
    const newItem = $('<li>Item</li>');

    // Append the new <li> element to the UL with the class my_list
    $('.my_list').append(newItem);
  });
});
