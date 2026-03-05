-- Write a SQL query to find the title of all TV shows and the name of their genres
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN genres g ON sg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
