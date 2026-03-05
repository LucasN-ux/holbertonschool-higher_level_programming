-- To create a MySQL database named `hbtn_0d_usa` and a table named `cities` with the following columns:
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;   
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    state_id INT,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
