-- Write a SQL query to find the name of all genres that the TV show "Dexter" belongs to. The tv_shows table has the following columns: id, title. The genres table has the following columns: id, name. The tv_show_genres table has the following columns: show_id, genre_id. The show_id column in the tv_show_genres table is a foreign key that references the id column in the tv_shows table. The genre_id column in the tv_show_genres table is a foreign key that references the id column in the genres table.
SELECT g.name
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN genres g ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
