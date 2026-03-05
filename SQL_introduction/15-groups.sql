-- To list all the scores in a MySQL table grouped by score, you can use the following command:
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
