-- Database: public

-- DROP DATABASE IF EXISTS public;

--CREATE DATABASE public
--    WITH
--    OWNER = postgres
--    ENCODING = 'UTF8'
--   LC_COLLATE = 'Hebrew_Israel.1252'
--   LC_CTYPE = 'Hebrew_Israel.1252'
--    LOCALE_PROVIDER = 'libc'
--    TABLESPACE = pg_default
--    CONNECTION LIMIT = -1
--    IS_TEMPLATE = False;

--CREATE TABLE items (
--	item_id SERIAL PRIMARY KEY,
--	item_type VARCHAR(100) NOT NULL,
--	item_price DECIMAL(10, 2) NOT NULL
--);

--INSERT INTO items (item_type,item_price)
--VALUES
--('Small Desk', 100),
--('Large desk', 300),
--('Fan', 80); 

--EXERCISE 1
--Fetch all items
--SELECT COUNT (*) AS total_rows
--from items;

--EXERCISE 2
-- Fetch all items with a price above 80 (80 not included)
--SELECT *
--FROM items
--WHERE item_price > 80;


--EXERCISE 3
--Fetch all items with a price below 300. (300 included)
SELECT *
FROM items
WHERE item_price <= 300;

