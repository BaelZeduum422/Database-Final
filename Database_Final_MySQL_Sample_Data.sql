USE Final_Database_Climate;

-- Insert Sample Data
INSERT INTO Continent (Continent_Name) VALUES 
('Antarctica'), ('Asia'), ('Africa'), ('Australia'), ('Europe'), ('North America'), ('South America');

INSERT INTO Hemisphere (Hemisphere_Name) VALUES 
('Northern Hemisphere'), ('Southern Hemisphere');

INSERT INTO Area (Hemisphere_ID, Continent_ID, Area_Name) VALUES
(1, 1, 'Japan'), (1, 2, 'France'), (2, 3, 'Canada'),
(2, 1, 'China'), (2, 2, 'Germany'), (1, 3, 'Mexico'),
(1, 1, 'Russia'), (1, 2, 'Italy'), (2, 3, 'Brazil'),
(2, 1, 'India'), (2, 2, 'Spain'), (1, 3, 'Western Australia'),
(1, 1, 'Sweden'), (1, 2, 'South Africa'), (2, 3, 'Argentina');

INSERT INTO YearlySeasonTemp (Area_ID, Year, Season, Temperature, Predicted_Temp) VALUES
(1, 2022, 'Spring', 20.5, 22.3), (2, 2022, 'Summer', 25.0, 26.5),
(3, 2022, 'Spring', 18.0, 19.5), (4, 2022, 'Summer', 27.5, 28.8),
(5, 2022, 'Spring', 21.8, 23.0), (6, 2022, 'Summer', 24.3, 25.8),
(7, 2022, 'Spring', 19.5, 21.0), (8, 2022, 'Summer', 26.8, 28.0),
(9, 2022, 'Spring', 22.0, 24.0), (10, 2022, 'Summer', 23.5, 24.8),
(11, 2022, 'Spring', 19.0, 20.5), (12, 2022, 'Summer', 25.2, 26.6),
(13, 2022, 'Spring', 17.8, 19.0), (14, 2022, 'Summer', 26.0, 27.5),
(15, 2022, 'Spring', 20.3, 21.8);
