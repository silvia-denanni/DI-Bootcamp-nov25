--CREATE TABLE FirstTab (
--     id integer, 
--     name VARCHAR(10)
--);

--INSERT INTO FirstTab VALUES
--(5,'Pawan'),
--(6,'Sharlee'),
--(7,'Krish'),
--(NULL,'Avtaar');

--SELECT * FROM FirstTab

--CREATE TABLE SecondTab (
--    id integer 
--);

--INSERT INTO SecondTab VALUES
--(5),
--(NULL);

--SELECT * FROM SecondTab


------------->Q1. What will be the OUTPUT of the following statement?----------->
-------------> the query returns 0 rows because the subquery returns a NULL, the NOT IN condition fails to match any rows
--SELECT COUNT(*) 
--  FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )


------------->Q2. What will be the OUTPUT of the following statement?
------------> the subquery returns 5 from SecondTab, ft.id NOT IN (5) -----> 2 ids
--SELECT COUNT(*) 
--    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

------------->Q3. What will be the OUTPUT of the following statement?
------------> the subquery returns 5 and NULL, NOT IN with a list containing NULL ---> ft.id <> 5 AND ft.id <> NULL ----> 
------------> ft.id <> NULL is UNKNOWN -------->ft.id = 6 or 7, the condition is UNKNOWN ------------->
------------>ft.id = 5, 5 NOT IN (5, NULL) is false ---------->ft.id = NULL, NULL NOT IN (5, NULL) is also UNKNOWN--------->0
--SELECT COUNT(*) 
--    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

------------->Q4. What will be the OUTPUT of the following statement?
------------->the subquery returns 5, ft.id NOT IN (5) -----> 2 ids
 SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )