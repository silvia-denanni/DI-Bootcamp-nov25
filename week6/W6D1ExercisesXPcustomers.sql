-- Database: public

-- DROP DATABASE IF EXISTS public;

--CREATE DATABASE public
--    WITH
--    OWNER = postgres
--    ENCODING = 'UTF8'
--    LC_COLLATE = 'Hebrew_Israel.1252'
--    LC_CTYPE = 'Hebrew_Israel.1252'
--    LOCALE_PROVIDER = 'libc'
--    TABLESPACE = pg_default
--    CONNECTION LIMIT = -1
--    IS_TEMPLATE = False;

--CREATE TABLE customers (
--cust_id SERIAL PRIMARY KEY,
--cust_name VARCHAR(50) NOT NULL,
--cust_surname VARCHAR(100) NOT NULL
--);

--INSERT INTO customers(cust_name,cust_surname)
--VALUES
--('Greg ', 'Jones'),
--('Sandra', 'Jones'),
--('Scott', 'Scott'),
--('Trevor', 'Green'),
--('Melanie', 'Johnson')


--EXERCISE 1
--Fetch all customers whose last name is ‘Smith’
--SELECT *
--FROM customers
--WHERE cust_surname = 'Smith'   ---> no one, nothing as a result


--EXERCISE 2
--Fetch all customers whose last name is ‘Jones’
--SELECT *
--FROM customers
--WHERE cust_surname = 'Jones'

--EXERCISE 3
--Fetch all customers whose-- cust_name is not ‘Scott’

SELECT *
FROM customers
WHERE cust_name != 'Scott'