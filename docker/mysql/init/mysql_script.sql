CREATE DATABASE IF NOT EXISTS grab;
USE grab;

CREATE TABLE IF NOT EXISTS drivers (
  id INT PRIMARY KEY,
  full_name VARCHAR(255),
  latitude DECIMAL(10,7),
  longitude DECIMAL(10,7)
);
