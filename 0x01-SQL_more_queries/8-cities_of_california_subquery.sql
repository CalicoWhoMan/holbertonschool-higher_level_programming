-- Script that lists all the Cities of California that is in the DB hbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
