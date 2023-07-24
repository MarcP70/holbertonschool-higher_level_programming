-- This script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Task 8.
-- Get the state_id for California using a subquery
SET @california_state_id := (SELECT id FROM states WHERE name = 'California');

-- Retrieve all cities of California using the state_id
SELECT * FROM cities WHERE state_id = @california_state_id ORDER BY id ASC;
