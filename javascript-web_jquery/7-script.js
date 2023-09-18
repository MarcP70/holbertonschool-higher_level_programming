// Task7: This script fetches the character name from this
// URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$(document).ready(function() {
    // URL to fetch character data
    const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    // Make an AJAX request to fetch character data
    $.ajax({
        url: apiUrl,
        type: 'GET',
        success: function(data) {
            // Update the content of the <div> with the character name
            $('#character').text(data.name);
        },
        error: function(error) {
            console.log('Error fetching the character name:', error);
        }
    });
});
