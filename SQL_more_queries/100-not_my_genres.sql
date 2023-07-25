-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- Task 17.
SELECT name
FROM tv_genres
WHERE id NOT IN (
    -- Subquery to get the genre_id linked to the show "Dexter"
    SELECT genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
