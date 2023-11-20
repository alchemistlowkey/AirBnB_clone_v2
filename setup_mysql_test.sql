-- Create a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant all privileges to the user on the hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select privilege to the user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush privileges to apply changes
FLUSH PRIVILEGES;
