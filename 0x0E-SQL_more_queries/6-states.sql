-- Script that creates a database and a table in it

-- Create database `hbtn_0d_usa`
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_usa;

-- Switch to the recently created database
USE hbtn_0d_usa;

-- Create table `states`
CREATE TABLE
	IF NOT EXISTS states(
		id INT NOT NULL AUTO_INCREMENT,
		name VARCHAR(256) NOT NULL,
		PRIMARY KEY(id)
		);
