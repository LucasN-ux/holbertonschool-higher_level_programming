-- Write a SQL query to find the name of each genre and the number of TV shows that belong to that genre.
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
GROUP BY g.id
HAVING COUNT(sg.show_id) > 0
ORDER BY number_of_shows DESC;
