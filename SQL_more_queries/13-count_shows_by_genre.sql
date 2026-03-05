-- Write a SQL query to find the name of each genre and the number of TV shows that belong to that genre. The genres table has the following columns: id, name. The tv_show_genres table has the following columns: show_id, genre_id. The genre_id column in the tv_show_genres table is a foreign key that references the id column in the genres table.
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres sg
ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;
