-- Create a MySQL server with:
--  A new user hbnb_dev (in localhost)
--  The password of hbnb_dev should be set to hbnb_dev_pwd
--  hbnb_dev should have all privileges on the database hbnb_dev_db
--  hbnb_dev should have SELECT privilege on the database performance_schema

-- Create the database if not found
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user if doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Commit all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;


