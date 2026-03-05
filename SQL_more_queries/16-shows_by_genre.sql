-- Write a SQL query to find the title of all TV shows and the name of their genres. The tv_shows table has the following columns: id, title. The genres table has the following columns: id, name. The tv_show_genres table has the following columns: show_id, genre_id. The show_id column in the tv_show_genres table is a foreign key that references the id column in the tv_shows table. The genre_id column in the tv_show_genres table is a foreign key that references the id column in the genres table.
SELECT s.title, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN genres g ON sg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
