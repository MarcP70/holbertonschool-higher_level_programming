// 100-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the elements with ids "add_item," "remove_item," and "clear_list"
  var addItemElement = document.getElementById('add_item');
  var removeItemElement = document.getElementById('remove_item');
  var clearListElement = document.getElementById('clear_list');
  
  // Select the <ul> element with class "my_list"
  var myListElement = document.querySelector('.my_list');

  // Function to add a new <li> element to the list
  function addItem() {
    var newListItem = document.createElement('li');
    newListItem.textContent = 'Item';
    myListElement.appendChild(newListItem);
  }

  // Function to remove the last <li> element from the list
  function removeItem() {
    var lastItem = myListElement.lastChild;
    if (lastItem) {
      myListElement.removeChild(lastItem);
    }
  }

  // Function to clear all <li> elements from the list
  function clearList() {
    myListElement.innerHTML = '';
  }

  // Add click event listeners to the respective elements
  addItemElement.addEventListener('click', addItem);
  removeItemElement.addEventListener('click', removeItem);
  clearListElement.addEventListener('click', clearList);
});
