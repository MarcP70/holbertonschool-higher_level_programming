// Task 10: This script updates the text color of the <header> element to red (#FF0000)
document.addEventListener('DOMContentLoaded', function() {
    // Select the <header> element
    const headerElement = document.querySelector('header');

    // Update the text color to red (#FF0000)
    if (headerElement) {
        headerElement.style.color = '#FF0000';
    }
});
