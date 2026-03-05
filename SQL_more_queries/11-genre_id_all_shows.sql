-- Write a SQL query to find the title and genre_id of all TV shows. The tv_shows table has the following columns: id, title. The tv_show_genres table has the following columns: show_id, genre_id. The show_id column in the tv_show_genres table is a foreign key that references the id column in the tv_shows table.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
