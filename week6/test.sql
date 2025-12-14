-------------->Table Creation ---------> CREATE TABLE
--CREATE TABLE actors (
--actor_id SERIAL PRIMARY KEY,   ---> SERIAL = (1,2,3,4....), ---> PRIMARY KEY = non null & unique
--first_name VARCHAR(50) NOT NULL,
--last_name VARCHAR(100) NOT NULL,
--birth_date DATE NOT NULL,
--oscar_number SMALLINT NOT NULL
--)


-------------->Visualizing Whole Table ---------> * SELECT * FROM
--SELECT * FROM actors  


-------------->Add Info ----------> INSERT INTO, VALUES
--INSERT INTO actors (first_name,last_name,birth_date, oscar_number)
--VALUES ('Matt', 'Damon', '08/10/1970', 5)

--SELECT * FROM actors


-------------->Add Info
--INSERT INTO actors (first_name,last_name,birth_date, oscar_number)
--VALUES ('Meryl', 'Streep', '22/06/1949', 3)


-------------->Add Info one by one ---------->
--INSERT INTO actors (first_name,last_name,birth_date, oscar_number)
--VALUES ('Emma', 'Stone', '06/11/1988', 2)


-------------->Add multiple rows at a time ---------->
--INSERT INTO actors(first_name,last_name,birth_date, oscar_number)
--VALUES
--('Heath', 'Ledger','04/04/1979', 1 ),
--('Christian', 'Bale','30/01/1974', 1 );


-------------->To select only 1 column ---------->SELECT columnname FROM tablename
--SELECT
--first_name
--FROM
--actors;

--------------->To select more columns at the same time ----> SELECT columnnames FROM tablename

--SELECT
--first_name,
--last_name,
--birth_date
--FROM
--actors;

--------------> To FILTER rows returned from the SELECT -----> SELECT*/columnname FROM tablename WHERE columnname condition (=, >,<, =<, =>, !=, AND, OR)
--------------> EXAMPLE: more than 2 oscars won
--SELECT *
--FROM actors
--WHERE oscar_number > 2;


--------------> EXAMPLE: showing all names, not Matt Damon's
--SELECT last_name
--FROM actors
--WHERE first_name != 'Matt';


--------------> EXAMPLE: select a specific actor/actress name
--SELECT first_name, last_name
--FROM actors
--WHERE first_name = 'Meryl' AND last_name = 'Streep'


--------------> EXAMPLE: name Matt OR oscars won 2
--SELECT first_name, last_name 
--FROM actors 
--WHERE first_name = 'Matt'  OR  oscar_number = 2 ;


-------------->Comparing a column to NULL ------------> IS NULL / IS NOT NULL
--------------> EXAMPLE: oscars won not NULL
--SELECT *
--FROM actors
--WHERE oscar_number IS NOT NULL;


--------------> Not Exactly Comparing --------------> LIKE (case sensitive!!!!!!!!!!!!!!!!!)
--------------> EXAMPLE: retrieve any record that has the string 'St' in it ----->
--SELECT * 
--FROM actors
--WHERE last_name LIKE '%St%';

--------------> EXAMPLE: retrieve all the last_names that END with “e”  ----->
--SELECT * 
--FROM actors
--WHERE last_name LIKE '%e'

--------------> EXAMPLE: retrieve names of actors whose last_names start with “St”  ----->
--SELECT first_name 
--FROM actors 
--WHERE last_name LIKE 'St%'

----------------> Not Exactly Comparing --------------> ILIKE (case insensitive!!!!!!!!!!!!!!!!!)
----------------> EXAMPLE: retrieve all the last_names that START with “da” 
--SELECT first_name
--FROM actors
--WHERE last_name ILIKE 'da%'


-------------->Limit Number of Retrieved Results to Specific Number --------> LIMIT
--------------> EXAMPLE: retrieve 1st actor

--SELECT *
--FROM actors
--LIMIT 1;

--------------> EXAMPLE: combine LIMIT with WHERE
--SELECT * 
--FROM actors
--WHERE birth_date = '30/01/1974' LIMIT 1;


-------------->Optional Keyword to Skip the First N Rows ----> OFFSET
--------------> EXAMPLE: skip the first two actors and display the next three actors
--SELECT *
--FROM actors
--WHERE birth_date > '30/01/1974' LIMIT 3 OFFSET 2;


----------> Sort the Retrieved Result ----------> ORDER BY in the SELECT statement in ascending or descending order based on the specified criteria
----------> EXAMPLE: all the actors ordered in ascending order of the first_name
--SELECT *
--FROM actors
--WHERE birth_date < '30/01/1974'
--ORDER BY first_name ASC

-------------> Change Record Values in a table ---------->UPDATE 
------------->EXAMPLE: Change the birthdate of ‘Matt Damon' and RETURNING the changed record
--UPDATE actors
--SET birth_date = '1970-01-01'
--WHERE first_name = 'Matt' AND last_name = 'Damon'
--RETURNING 
--actor_id,
--first_name,
--last_name,
--birth_date


-------------> 1) Delete Data from a table ---------->DELETE
-------------> EXAMPLE: delete all rows ----------> DELETE FROM table;

-------------> EXAMPLE: delete and return with DELETE + RETURNING----->
--DELETE FROM actors
--WHERE actor_id = 4
--RETURNING 
--actor_id, 
--first_name,
--last_name,
--oscar_number


-------------> 2) Delete Data from a table ---------->TRUNCATE
------------> E.G. TRUNCATE TABLE ----> removes all rows from a table without scanning it (
------> reclaims the storage right away, faster than DELETE)
 

-----------> EXAMPLE: add more records after deleting all the rows, 
------>the SERIAL column will start again from 1
--TRUNCATE actors
--RESTART IDENTITY                   ---->restarts the SERIAL column


------------> Remove Existing Table from DB ---------> DROP TABLE
-----------> EXAMPLE:
--DROP TABLE IF EXISTS actors;



-----------------> Change Existing Table Structure ------> ALTER TABLE
-----------> EXAMPLE: Add new column 
ALTER TABLE actors ADD COLUMN is_alive BOOLEAN;
SELECT * FROM actors

-----------> EXAMPLE: Remove Existing Column
--ALTER TABLE actors
--DROP COLUMN columnName

-----------> EXAMPLE: Rename Existing Column
--ALTER TABLE actors
--RENAME COLUMN columnName TO newColumnName

-----------> EXAMPLE: Rename Existing Table
--ALTER TABLE actors
---RENAME TO newTableName

-----------> EXAMPLE: Change Column Data Yype
--ALTER TABLE actors
--ALTER COLUMN columnName1 [SET DATA] TYPE newDataType;
