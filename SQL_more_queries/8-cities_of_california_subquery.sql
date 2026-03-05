-- Write a SQL query to find the id and name of all cities in California. The states table has the following columns: id, name. The cities table has the following columns: id, name, state_id. The state_id column in the cities table is a foreign key that references the id column in the states table.
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = "California"
)
ORDER BY id ASC;