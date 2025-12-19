----------->Part 1

----------->Create 2 tables : Customer and Customer profile. They have a One to One relationship.
----------->A customer can have only one profile, and a profile belongs to only one customer.
----------->The Customer table should have the columns : id, first_name, last_name NOT NULL
----------->The Customer profile table should have the columns : id, isLoggedIn DEFAULT false(Boolean)
----------->customer_id (a reference to the Customer table)


----------- Drop tables if they exist to allow rerunning the script without errors
-- DROP TABLE IF EXISTS customer_profile;
-- DROP TABLE IF EXISTS customer;


----------- Create Customer table

-- CREATE TABLE customer(
-- 	cust_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL
-- );

----------- Create Customer Profile table with one-to-one relationship to Customer

-- CREATE TABLE customer_profile (
-- 	cust_id INTEGER PRIMARY KEY,
-- 	isLoggedIn BOOLEAN DEFAULT FALSE,
-- 	CONSTRAINT fk_customer
-- 		FOREIGN KEY (cust_id) REFERENCES customer (cust_id) 
-- 		ON DELETE CASCADE --------------------> if a customer is deleted, their profile as well automatically
-- );

--------->Insert customers into 'customer'
-- INSERT INTO customer(first_name, last_name)
-- VALUES
-- 	('John','Doe'),
-- 	('Jerome','Lalu'),
-- 	('Lea','Rive');

----------->Insert profiles into 'customer_profile'
-- INSERT INTO customer_profile(cust_id, isLoggedIn)
-- VALUES
-- (
-- 	(SELECT cust_id FROM customer WHERE first_name = 'John' AND last_name = 'Doe'),
-- 	TRUE
-- ),
-- (
-- 	(SELECT cust_id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'),
-- 	FALSE
-- );

	
------------->Use the relevant types of Joins to display:
-- The first_name of the LoggedIn customers
-- All the customers first_name and isLoggedIn columns - even those who don’t have a profile.
-- The number of customers that are not LoggedIn

------------ Query 1: Get first names of customers who are logged in

-- SELECT c.first_name
-- FROM customer AS c
-- INNER JOIN customer_profile AS cp ON c.cust_id = cp.cust_id  ---------> get customers with profiles where isLoggedIn is true          
-- WHERE cp.isLoggedIn = TRUE;


------------ Query 2: Get all customers with their login status, including those without profiles

-- SELECT c.first_name, cp.isLoggedIn
-- FROM customer AS c
-- LEFT JOIN customer_profile AS cp ON c.cust_id = cp.cust_id --------->from 'customer' to 'customer_profile' including all customers

----------- Query 3: Count customers who are not logged in or have no profile
-- SELECT COUNT(*) AS not_logged_in_count
-- FROM customer AS c
-- LEFT JOIN customer_profile AS cp ON c.cust_id = cp.cust_id
-- WHERE cp.isLoggedIn = FALSE OR cp.isLoggedIn ISNULL; --------------->customers who do not have 
--                                                  profile (because the join didn't find a match).


----------->Part 2
----------->Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT
-------NULL, author NOT NULL, FILL IT AS TOLD
----------->Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, 
-------name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 
-------(Find an SQL method), FILL IT AS TOLD
----------->Create a table named Library, with the columns AS TOLD

-------------Drop tables if they exist to allow rerunning the script without errors
-- DROP TABLE IF EXISTS library;
-- DROP TABLE IF EXISTS student;
-- DROP TABLE IF EXISTS book;

-- CREATE TABLE book(
-- 	book_id SERIAL PRIMARY KEY,
-- 	title VARCHAR(50) NOT NULL,
-- 	author VARCHAR(50) NOT NULL
-- );

-- INSERT INTO book(title, author)
-- VALUES 	
-- 	('Alice In Wonderland','Lewis Carroll'),
-- 	('Harry Potter','J.K Rowling'),
-- 	('To kill A Mockingbird', 'Harper Lee');

-- CREATE TABLE student(
-- 	student_id SERIAL PRIMARY KEY,
--  stud_name VARCHAR(50) NOT NULL UNIQUE,
-- 	stud_age SMALLINT NOT NULL CONSTRAINT age_check CHECK (stud_age <= 15)   --stronger than 'stud_age SMALLINT NOT NULL DEFAULT 15'
-- );

-- INSERT INTO student(stud_name, stud_age)
-- VALUES 	
-- 	('John','12'),
-- 	('Lera','11'),
-- 	('Patrick', '10'),
-- 	('Bob', '14');

--JUNCTION TABLE: -----------------> many-to-many relationships

-- CREATE TABLE library (
--   book_fk_id INTEGER NOT NULL,
--   student_fk_id INTEGER NOT NULL,
--   borrowed_date DATE NOT NULL,
--   PRIMARY KEY (book_fk_id, student_fk_id),
--   FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
--   FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- ); --------------------->If a book or student is deleted or their IDs updated, 
-- ------------------------the related rows in library will be automatically deleted or updated.


-- INSERT INTO library (book_fk_id, student_fk_id, borrowed_date) VALUES
--   (
--     (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
--     (SELECT student_id FROM student WHERE stud_name = 'John'),
--     '2022-02-15'
--   ),
--   (
--     (SELECT book_id FROM book WHERE title = 'To kill A Mockingbird'),
--     (SELECT student_id FROM student WHERE stud_name = 'Bob'),
--     '2021-03-03'
--   ),
--   (
--     (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
--     (SELECT student_id FROM student WHERE stud_name = 'Lera'),
--     '2021-05-23'
--   ),
--   (
--     (SELECT book_id FROM book WHERE title = 'Harry Potter'),
--     (SELECT student_id FROM student WHERE stud_name = 'Bob'),
--     '2021-08-12'
--   );


--SELECT * FROM library


-- SELECT s.stud_name AS student_name, b.title AS book_title
-- FROM library l
-- JOIN student s ON l.student_fk_id = s.student_id
-- JOIN book b ON l.book_fk_id = b.book_id;

SELECT AVG(s.stud_age) AS avg_age
FROM library AS l
JOIN student AS s ON l.student_fk_id = s.student_id
JOIN book AS b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland'


-- Because the foreign key constraint on student_fk_name in the library table uses ON DELETE CASCADE,
-- when you delete a student from the student table, all rows in the library table that reference

-- that student will be automatically deleted.
