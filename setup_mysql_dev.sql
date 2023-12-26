-- Create a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant all privileges to the user on the hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grant select privilege to the user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Flush privileges to apply changes
FLUSH PRIVILEGES;
