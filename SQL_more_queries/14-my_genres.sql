-- Write a SQL query to find the name of all genres that the TV show "Dexter" belongs to.
SELECT g.name
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN genres g ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
