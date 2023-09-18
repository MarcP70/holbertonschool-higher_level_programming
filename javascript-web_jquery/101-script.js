// Task11: This script adds, removes and clears LI elements from a list when the user clicks
$(document).ready(function() {
    // Function to add a new <li> item to the list
    $('#add_item').click(function() {
        const newItem = $('<li>Item</li>');
        $('.my_list').append(newItem);
    });

    // Function to remove the last <li> item from the list
    $('#remove_item').click(function() {
        $('.my_list li:last-child').remove();
    });

    // Function to clear all <li> items from the list
    $('#clear_list').click(function() {
        $('.my_list').empty();
    });
});
