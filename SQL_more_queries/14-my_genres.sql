-- This script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Task 14.
SELECT tv_genres.name
from tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
