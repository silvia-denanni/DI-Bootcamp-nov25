-- RELATIONSHIPS BETWEEN TABLES

--ONE TO ONE = THE PK OF THE PARENT IS THE FK OF THE CHILD

-- SELECT * FROM movies


-- CREATE TABLE scenarios(
-- pk_movie_id INTEGER NOT NULL,
-- scenario_description TEXT NOT NULL, 
-- PRIMARY KEY (pk_movie_id),
-- CONSTRAINT fk_movie_id FOREIGN KEY (pk_movie_id) REFERENCES movies (movie_id)
-- )

-- INSERT INTO scenarios (pk_movie_id, scenario_description)
-- VALUES
-- ((SELECT movie_id FROM movies WHERE movie_title = 'Good Will hunting'),
-- 'An University in England'),
-- ((SELECT movie_id FROM movies WHERE movie_title = 'Harry Potter and the philosophars stone'),
-- 'Hogwarts School of Witchcraft and Wizardry');

-- SELECT * FROM scenarios


-- ONE TO MANY = PK OF THE PARENT IS RELATED TO MANY ROWS ON THE FK OF THE CHILD

--PARENT TABLE (ONE)
-- CREATE TABLE directors (
--   director_id SERIAL,
--   first_name VARCHAR(30) NOT NULL,
--   last_name VARCHAR(30) NOT NULL,
--   PRIMARY KEY (director_id)
-- );


--CHILD TABLE (MANY)

-- CREATE TABLE movies_2 (
--   movie_id SERIAL,
--   movie_title VARCHAR(45) NOT NULL,
--   released_date date NOT NULL,
--   fk_director_id INTEGER NOT NULL,
--   PRIMARY KEY (movie_id),
--   FOREIGN KEY (fk_director_id) REFERENCES directors(director_id) ON DELETE CASCADE
-- );

-- INSERT INTO directors (first_name, last_name)
-- VALUES
-- ('Steven', 'Spielberg'),
-- ('Christopher', 'Nolan'),
-- ('Quentin', 'Tarantino')

-- INSERT INTO movies_2 (movie_title, released_date, fk_director_id)
-- VALUES
-- ('Interstellar', '01/01/2014', (SELECT director_id FROM directors WHERE first_name = 'Christopher')),
-- ('The Dark Knight', '05/12/2012', (SELECT director_id FROM directors WHERE first_name = 'Christopher')),
-- ('E.T', '10/06/1982', (SELECT director_id FROM directors WHERE first_name = 'Steven'))

-- SELECT * FROM movies_2

-- MANY TO MANY = REPRESENTED BY A JUNCTION TABLE

--JUNCTION TABLE:
-- CREATE TABLE actors_movies (
-- actor_id INTEGER NOT NULL,
-- movie_id INTEGER NOT NULL,
-- actor_role VARCHAR(30) NOT NULL,
-- is_lead_role BOOLEAN NOT NULL,
-- PRIMARY KEY (actor_id, movie_id),
-- FOREIGN KEY (actor_id) REFERENCES actors(actors_id) ON UPDATE CASCADE,
-- FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON UPDATE CASCADE
-- )



-- INSERT into actors_movies(actor_id, movie_id, actor_role, is_lead_role) 
-- VALUES 
-- (
-- (SELECT actors_id FROM actors WHERE first_name = 'Matt' AND last_name = 'Damon'),
-- (SELECT movie_id FROM movies WHERE movie_title = 'Good Will hunting'), 
-- 'Will Hunting', True),

-- (
-- (SELECT actors_id FROM actors WHERE first_name = 'Meryl'),
-- (SELECT movie_id FROM movies WHERE movie_title = 'The Devil wears Prada'), 
-- 'Miranda', False),

-- (
-- (SELECT actors_id FROM actors WHERE first_name = 'Matt' AND last_name = 'Damon'),
-- (SELECT movie_id FROM movies WHERE movie_title = 'Oceans Eleven'), 
-- 'John', False);

-- SELECT * FROM actors_movies

