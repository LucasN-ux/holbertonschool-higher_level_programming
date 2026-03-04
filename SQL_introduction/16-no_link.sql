-- To list all the scores in a MySQL table that are not NULL or empty, you can use the following command:
SELECT score, name 
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
