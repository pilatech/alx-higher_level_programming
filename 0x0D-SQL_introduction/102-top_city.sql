-- display average temperatures by city in descending order
-- list city and average temperature
SELECT city, SUM(value) AS avg_temp FROM temperatures
GROUP BY city
WHERE month=7 AND month=8
ORDER BY avg_temp DESC LIMIT 3;
