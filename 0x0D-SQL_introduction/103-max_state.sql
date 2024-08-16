-- display maximum temperature for each state ordered by State
-- list state and max temperature
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
