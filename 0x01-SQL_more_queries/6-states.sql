-- Script that creates the DB 'hbtn_0d_usa' & Table 'states'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states
	(id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));
