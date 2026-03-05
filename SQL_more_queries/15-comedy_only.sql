-- Write a SQL query to find the title of all TV shows that belong to the "Comedy" genre
SELECT s.title
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
