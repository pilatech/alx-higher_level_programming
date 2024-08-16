-- display average temperatures by city in descending order
-- list city and average temperature
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month IN(7, 8)
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
