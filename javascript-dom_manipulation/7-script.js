// 7-script.js
document.addEventListener('DOMContentLoaded', function () {
  // Select the <ul> element with the id "list_movies"
  var listMoviesElement = document.getElementById('list_movies');

  // Fetch the list of Star Wars movies from the URL
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function (response) {
      // Check if the response is successful (status code 200)
      if (response.status === 200) {
        // Parse the response JSON
        return response.json();
      } else {
        throw new Error('Failed to fetch movie data');
      }
    })
    .then(function (data) {
      // Iterate through the movie data and extract titles
      data.results.forEach(function (movie) {
        var movieTitle = movie.title;
        
        // Create a new <li> element for each movie title
        var listItem = document.createElement('li');
        listItem.textContent = movieTitle;
        
        // Append the <li> element to the <ul> list
        listMoviesElement.appendChild(listItem);
      });
    })
    .catch(function (error) {
      console.error(error);
    });
});
