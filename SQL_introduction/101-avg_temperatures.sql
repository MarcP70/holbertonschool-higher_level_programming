-- This script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Task 18.
SELECT city, ROUND(AVG(value), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
