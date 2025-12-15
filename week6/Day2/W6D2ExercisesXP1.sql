------------->Exercise 1 : Items and customers
------------->Count all items
--SELECT COUNT (*) AS total_rows FROM items; 

------------->All items, ordered by price (lowest to highest).
--SELECT * FROM items ORDER BY item_price ASC

------------->Items with a price above 80 (80 included), ordered by price (highest to lowest).
--SELECT * FROM items
--WHERE item_price >= 80
--ORDER BY item_price DESC 

------------->The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
--SELECT cust_name
--FROM customers
--ORDER BY cust_name ASC
--LIMIT 3;

------------->All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT cust_surname
FROM customers
ORDER BY cust_surname DESC