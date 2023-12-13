-- Create Database
CREATE DATABASE IF NOT EXISTS Final_Database_Climate;

-- Use Database
USE Final_Database_Climate;

-- Create Tables
CREATE TABLE Continent (
    Continent_ID INT AUTO_INCREMENT PRIMARY KEY,
    Continent_Name VARCHAR(255) NOT NULL
);

CREATE TABLE Hemisphere (
    Hemisphere_ID INT AUTO_INCREMENT PRIMARY KEY,
    Hemisphere_Name VARCHAR(255) NOT NULL
);

CREATE TABLE Area (
    Area_ID INT AUTO_INCREMENT PRIMARY KEY,
    Hemisphere_ID INT,
    Continent_ID INT,
    Area_Name VARCHAR(255) NOT NULL,
    FOREIGN KEY (Hemisphere_ID) REFERENCES Hemisphere(Hemisphere_ID),
    FOREIGN KEY (Continent_ID) REFERENCES Continent(Continent_ID)
);

CREATE TABLE YearlySeasonTemp (
    YearlyTemp_ID INT AUTO_INCREMENT PRIMARY KEY,
    Area_ID INT,
    Year INT,
    Season VARCHAR(50),
    Temperature DECIMAL(5,2),
    Predicted_Temp DECIMAL(5,2),
    UNIQUE KEY `Area_Year_Season` (`Area_ID`, `Year`, `Season`), -- Composite Unique Key
    FOREIGN KEY (Area_ID) REFERENCES Area(Area_ID)
);

-- Create User and Grant Permissions
CREATE USER 'User_Access'@'127.0.0.1' IDENTIFIED BY 'Incorrect';
GRANT ALL PRIVILEGES ON Final_Database_Climate.* TO 'User_Access'@'127.0.0.1';
FLUSH PRIVILEGES;
