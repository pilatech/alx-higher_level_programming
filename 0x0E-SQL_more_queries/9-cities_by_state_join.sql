-- Script to list cities in cities table using LEFT JOIN

-- list the cities
SELECT cities.id AS id,
	   cities.name AS name,
	   states.name AS name
  FROM cities
LEFT JOIN states 
       ON cities.state_id = states.id
 ORDER BY cities.id;
