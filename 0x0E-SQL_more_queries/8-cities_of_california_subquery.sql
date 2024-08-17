-- Script to list cities in cities table using subquery

-- list the cities
SELECT *
  FROM cities
 WHERE state_id = (
	SELECT id
	  FROM states
	 WHERE name = 'California'
	 LIMIT 1
	)
ORDER BY cities.id;
