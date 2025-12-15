--FOREIGN KEY EXAMPLE

--DROP TABLE IF EXISTS MOVIES;

--CREATE TABLE MOVIES (
--	MOVIE_ID SERIAL PRIMARY KEY,
--	MOVIE_TITLE VARCHAR(100) NOT NULL,
--	MOVIE_STORY TEXT,
--	ACTOR_PLAYING_ID INTEGER,
--	FOREIGN KEY (ACTOR_PLAYING_ID) REFERENCES ACTORS (ACTOR_ID)
--);

--INSERT INTO movies (movie_title, movie_story, actor_playing_id)
--VALUES
--('Good Will Hunting',
--'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting.',
--5);
--SELECT * FROM movies;

--INSERT INTO movies (movie_title, movie_story, actor_playing_id)
--VALUES
--(
--  'Good Will Hunting',
--  'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting.',
--  (SELECT actor_id FROM actors WHERE first_name='Matt' AND last_name='Damon')
--),
--(
--  'Oceans Eleven',
--  'American heist film directed by Steven Soderbergh and written by Ted Griffin.',
--  (SELECT actor_id FROM actors WHERE first_name='Matt' AND last_name='Damon')
--);


----------------------->INNER JOIN ----------->it doesn't create a table, it displays related data (not null values)
-------------------->ALIAS "AS" --------------> JUST FOR DISPLAY, to be faster
--SELECT a.first_name, a.last_name, m.movie_title
--FROM actors AS a
--INNER JOIN movies AS m
--ON a.actor_id = m.actor_playing_id;


----------------------->FULL JOIN ----------->SHOWS DATA OF BOTH TABLES (even if NULL)

--SELECT actors.first_name, actors.last_name, movies.movie_title
--FROM actors
--FULL JOIN movies
--ON actors.actor_id = movies.actor_playing_id;


----------------------->LEFT JOIN ----------->SHOWS DATA OF LEFT TABLE (even if NULL)
--SELECT actors.first_name, actors.last_name, movies.movie_title
--FROM actors
--LEFT JOIN movies
--ON actors.actor_id = movies.actor_playing_id;

----------------------->RIGHT JOIN ----------->SHOWS DATA OF RIGHT TABLE (even if NULL)
--SELECT actors.first_name, actors.last_name, movies.movie_title
--FROM actors
--LEFT JOIN movies
--ON actors.actor_id = movies.actor_playing_id;

--------CORRECTING Christian Bale mistake--------------------------------
--UPDATE movies
--SET actor_playing_id = (SELECT actor_id FROM actors WHERE first_name='Matt' AND last_name='Damon')
--WHERE movie_title = 'Good Will Hunting';

--------CORRECTING duplicated 'Good Will Hunting' movie mistake--------------------------------
--DELETE FROM movies
--WHERE movie_title = 'Good Will Hunting' AND movie_id = 2


--INSERT INTO movies (movie_title, movie_story, actor_playing_id)
--VALUES
--(
  --'The Devil Wears Prada',
  --'Andy is a recent college graduate with big dreams. Upon landing a job at prestigious Runway magazine, she finds herself the assistant to diabolical editor Miranda Priestly. Andy questions her ability to survive her grim tour as a whipping girl without getting scorched.',
  --(SELECT actor_id FROM actors WHERE first_name='Meryl' AND last_name='Streep')
--);


----------------------->INNER JOIN ----------->

--SELECT actors.first_name, actors.last_name, movies.movie_title
--FROM actors
--INNER JOIN movies
--ON actors.actor_id = movies.actor_playing_id;

---------EXERCISE ---------------'JOINS' can all be used WITHOUT Foreign Key!!!!!!!!!!!!!!!

--CREATE TABLE countries (
--country_id SERIAL PRIMARY KEY,
--country_name VARCHAR(50) NOT NULL
--);

--INSERT INTO countries (country_name)
--VALUES
--('Israel'), ('Brazil'),('USA'), ('Ukraine')

--SELECT * FROM countries

----------------------->INNER JOIN ----------->

--SELECT countries.country_name, countries.country_id, actors.last_name, actors.actor_id
--FROM countries
--FULL JOIN actors
--ON actors.actor_id = country_id;


--------------------ALIAS together with CONCATENATE || ' ' ||-----------

--SELECT first_name || ' ' || last_name AS full_name FROM actors


--------------------AGGREGATE FUNCTIONS--------------

--SELECT AVG(oscar_number) AS average_oscar_number FROM actors

--SELECT MIN(oscar_number) FROM actors

------------------EXAMPLE: TO SEE ALSO THE ACTORS NAME IN MIN AGG FUNC
--SELECT first_name, last_name, oscar_number
--FROM actors
--WHERE oscar_number = (SELECT MIN(oscar_number) FROM actors)


-------------------EXAMPLE: TO SEE ALL OF THE OSCARS IN THE DB
SELECT SUM(oscar_number) AS total_oscars FROM actors
