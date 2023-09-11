// 4-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the element with the id "add_item"
  var addItemElement = document.getElementById('add_item');

  // Add a click event listener to the selected element
  addItemElement.addEventListener('click', function () {
    // Create a new <li> element
    var newListItem = document.createElement('li');
    
    // Set the text content of the new element
    newListItem.textContent = 'Item';

    // Select the <ul> element with class "my_list"
    var myListElement = document.querySelector('.my_list');
    
    // Append the new <li> element to the <ul> element
    myListElement.appendChild(newListItem);
  });
});
