-- Create a MYSQL server with:
--  A database hbnb_test_db
--  A new user hbnb_test (in localhost)
--  hbnb_test should have all privileges on the database hbnb_test_db
--  hbnb_test should have SELECT privilege on the database performance_schema

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to aplly changes
FLUSH PRIVILEGES;
