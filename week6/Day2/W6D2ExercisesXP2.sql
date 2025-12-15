------------>EX.1 In the dvdrental database write a query to select all the columns from the “customer” table.
--SELECT * from customer

------------>EX.2 Write a query to display the names (first_name, last_name) using an alias named “full_name”.
--SELECT first_name || ' ' || last_name AS full_name FROM customer

------------>EX.3 Lets get all the dates that accounts were created. Write a query to select all the create_date
------------from the “customer” table (there should be no duplicates).
--SELECT DISTINCT create_date
--FROM customer;

------------>EX.4 Write a query to get all the customer details from the customer table, it should be displayed
------------in descending order by their first name.

--SELECT first_name, last_name, email, address_id
--FROM customer
--ORDER BY first_name DESC 

------------>EX.5 Write a query to get the film_id, title, description, release_year and rental_rate 
------------in ascending order according to their rental rate.

--SELECT film_id, title, description, release_year, rental_rate
--FROM film
--ORDER BY rental_rate ASC;

------------>EX.6 Write a query to get the address, and the phone number of all customers living in 
------------the Texas district, these details can be found in the “address” table.
--SELECT address, phone, district
--FROM address
--WHERE district ILIKE '%tex%'


----------->EX.7 Write a query to retrieve all movie details where the movie id is either 15 or 150
--SELECT film_id, title, description, release_year, length, language_id, rating, special_features
--FROM film
--WHERE film_id = 15 OR film_id = 150


-----------> EX.8 Write a query which should check if your favorite movie exists in the database. 
-----------Have your query get the film ID, title, description, length and the rental rate, 
-----------these details can be found in the “film” table.
--SELECT film_id, title, description, length, rental_rate
--FROM film
--WHERE title = 'Donnie Darko';

-----------> EX.9 No luck finding your movie? Maybe you made a mistake spelling the name. 
-----------Write a query to get the film ID, title, description, length and the rental rate
-----------of all the movies starting with the two first letters of your favorite movie.

--SELECT film_id, title, description, length, rental_rate
--FROM film
--WHERE title LIKE 'Do%'

-----------> EX.10 Write a query which will find the 10 cheapest movies.

--SELECT DISTINCT replacement_cost
--FROM film
--ORDER BY replacement_cost ASC 
--LIMIT 10;

-----------> EX.11 Not satisfied with the results. Write a query which will find
-----------the next 10 cheapest movies without using limit

--SELECT DISTINCT replacement_cost
--FROM film
--ORDER BY replacement_cost ASC
--OFFSET 10 ROWS
--FETCH NEXT 10 ROWS ONLY;


-----------> EX.12 Write a query which will join the data in the customer table and the 
-----------payment table. You want to get the first name and last name from the curstomer table,
-----------as well as the amount and the date of every payment made by a customer, 
-----------ordered by their id (from 1 to…).

--SELECT DISTINCT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date
--FROM customer AS c
--INNER JOIN payment AS p ON p.customer_id = c.customer_id
--ORDER BY c.customer_id ASC;


---------->EX. 13 You need to check your inventory. Write a query to get all the movies 
-----------which are not in inventory.

--SELECT f.film_id, title
--FROM film as f
--LEFT JOIN inventory as i ON f.film_id = i.film_id
--WHERE i.film_id IS NULL;


---------->EX. 14 Write a query to find which city is in which country.
--SELECT city.city, city.country_id, country.country_id, country.country
--FROM city
--LEFT JOIN country ON city.country_id = country.country_id

---------->EX. 15 Write a query to get the customer’s id, names (first and last),
-----------the amount and the date of payment ordered by the id of the staff member
-----------who sold them the dvd.

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.customer_id, p.staff_id
FROM customer AS c
LEFT JOIN payment as p ON c.customer_id = p.customer_id
ORDER BY p.staff_id 


