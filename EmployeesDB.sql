CREATE DATABASE employees;

USE employees;

CREATE TABLE login_details (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  employee_id VARCHAR(20) NOT NULL,
  contact_number VARCHAR(20) NOT NULL,
  profile_picture BLOB,
  email_id VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  employee_type VARCHAR(20) NOT NULL,
  vehicle_id VARCHAR(20) NOT NULL
);