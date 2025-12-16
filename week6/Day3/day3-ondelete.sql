-- once the tables are connected (relationships) 
-- we need to define what will happen on the child table/s 
-- if a record is deleted or updated on the parent table

-- WE HAVE A COUPLE OPTIONS:

-- ON DELETE RESTRICT = DOESN'T ALLOW TO DELETE A RECORD IF THERE ARE 
-- RELATED ROWS

-- DELETE FROM actors WHERE first_name = 'Meryl' - IT GIVES AN ERROR

--CASCADE = THE RELATED ROWS OF THAT RECORD WILL ALSO BE DELETED OR UPDATED

-- CREATE TABLE colors (
-- color_id SERIAL PRIMARY KEY,
-- color_name VARCHAR (20) NOT NULL
-- );

-- ALTER TABLE color RENAME COLUMN color_if TO color_id



-- CREATE TABLE cars_default (
-- car_id SERIAL PRIMARY KEY,
-- car_name VARCHAR(50) NOT NULL, 
-- car_color INTEGER DEFAULT 4 REFERENCES colors (color_id) ON DELETE SET DEFAULT);

-- -- -- INSERT INTO colors (color_name)
-- -- -- VALUES ('black');

-- INSERT INTO cars_default (car_name, car_color)
-- VALUES 
-- ('Ferrari', (SELECT color_id FROM colors WHERE color_name = 'grey')),
-- ('Porsch', (SELECT color_id FROM colors WHERE color_name = 'black')),
-- ('Mazda', (SELECT color_id FROM colors WHERE color_name = 'grey'));



-- DELETE FROM colors WHERE color_name = 'grey';

-- SELECT * FROM cars_default