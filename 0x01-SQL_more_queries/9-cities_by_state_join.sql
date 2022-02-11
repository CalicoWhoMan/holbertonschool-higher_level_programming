-- Script that lists all cities in DB hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON states.id = cities.state_id
ORDER BY id ASC;
