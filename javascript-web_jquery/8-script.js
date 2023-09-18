// Task8: This script  fetches and lists the title for all movies by using
// this URL: https://swapi-api.hbtn.io/api/films/?format=json
$(document).ready(function() {
    // URL to fetch Star Wars movies data
    const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

    // Make an AJAX request to fetch Star Wars movies data
    $.ajax({
        url: apiUrl,
        type: 'GET',
        success: function(data) {
            // Update the content of the <ul> with the movie titles
            const listMovies = $('#list_movies');
            data.results.forEach(function(movie) {
                listMovies.append('<li>' + movie.title + '</li>');
            });
        },
        error: function(error) {
            console.log('Error fetching Star Wars movies data:', error);
        }
    });
});
