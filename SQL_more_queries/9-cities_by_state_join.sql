-- Write a SQL query to find the id and name of all cities, along with the name of their corresponding state. The states table has the following columns: id, name. The cities table has the following columns: id, name, state_id. The state_id column in the cities table is a foreign key that references the id column in the states table.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
