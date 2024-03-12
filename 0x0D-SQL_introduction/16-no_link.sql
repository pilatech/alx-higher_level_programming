-- list all records from the second_database
-- list records.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
