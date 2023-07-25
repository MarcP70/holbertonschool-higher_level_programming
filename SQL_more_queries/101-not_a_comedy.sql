-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Task 18.
SELECT title
from tv_shows
WHERE id NOT IN (
    SELECT show_id
    FROM tv_show_genres
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE name = 'Comedy'
)
ORDER BY title ASC;
