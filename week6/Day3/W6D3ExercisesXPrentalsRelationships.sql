----------------> Extra exercise

-- SELECT COUNT (*) AS title_count
-- FROM film AS f
-- JOIN language as l ON f.language_id = l.language_id
-- WHERE l.name = 'English'


----------------> Exercise 1  DVD Rental
-----------------Get a list of all the languages, from the language table.
-- SELECT name FROM language


----------------Get a list of all films joined with their languages – select the following details : film title, description, and language name.
-- SELECT f.title, f.description, l.name
-- FROM film as f
-- JOIN language AS l ON f.language_id = l.language_id

----------------Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
-- SELECT f.title,f.description, l.name
-- FROM language AS l
-- LEFT JOIN film AS f ON f.language_id = l.language_id


----------------Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- CREATE TABLE new_films(
-- film_id SERIAL PRIMARY KEY,
-- film_name VARCHAR(50) NOT NULL UNIQUE,
-- film_lang VARCHAR(50) NOT NULL
-- );

-- INSERT INTO new_films(film_name, film_lang )
-- VALUES
-- ('Donnie Darko', 'English'),
-- ('American Beauty', 'English'),
-- ('Le Diner Des Cons', 'French'),
-- ('Battle Royale', 'Japanese'),
-- ('Life Is Beautiful', 'Italian')


--------------Create a new table called new_film with the following columns : id, name. Add some new films to the table.
-- CREATE TABLE customer_review(
--   review_id SERIAL PRIMARY KEY,
--   new_films_fk_id INTEGER NOT NULL,
--   language_fk_id INTEGER NOT NULL,
--   rev_title VARCHAR(50) NOT NULL,
--   score SMALLINT CHECK (score >= 1 AND score <= 10),
--   review_text TEXT,
--   last_update DATE,
--   FOREIGN KEY (new_films_fk_id) REFERENCES new_films(film_id),
--   FOREIGN KEY (language_fk_id) REFERENCES language(language_id)
-- );

-------------Drop the existing foreign key constraint 
-- ALTER TABLE customer_review
-- DROP CONSTRAINT customer_review_new_films_fk_id_fkey;

-------------Add the foreign key constraint with ON DELETE CASCADE
-- ALTER TABLE customer_review
-- ADD CONSTRAINT customer_review_new_films_fk_id_fkey
-- FOREIGN KEY (new_films_fk_id) REFERENCES new_films(film_id) ON DELETE CASCADE;

-- INSERT INTO customer_review (new_films_fk_id, language_fk_id, rev_title, review_text, score) VALUES
-- (
--   (SELECT film_id FROM new_films WHERE film_name = 'Donnie Darko'),
--   (SELECT language_id FROM language WHERE name = 'English'),
--   'Mind blowing story',
--   'Many say that Donnie Darko is one of the best films of all time ... and I tend to believe that, he manages to create suspense, tension, well written and well crafted. I couldn''t help but notice how good acting is, Jake Gyllenhaal, Drew Barrymore, Maggie Gyllenhaal, Seth Rogen, Patrick Swayze, and many others do an exceptional job. The soundtrack is so euphoric, the movie is unique, delves into odd things about timetravel, but manages to keep you interested. Over-all a superb movie',
--    10,
--    current_date
--   ),
-- (
--   (SELECT film_id FROM new_films WHERE film_name = 'Battle Royale'),
--   (SELECT language_id FROM language WHERE name = 'Japanese'),
--   'An aesthetically gorgeous brutal survival movie.',
--   'A tantalizing aesthetic runs through the film defying categorization. At first the theme is the suspension of all morality, first on the part of a demented governmental scheme followed by the replication of this nihilism among the captive students. Then as alliances forge and melt into oblivion a hopeful air in the film arises. Inter titles are used to comic excess, something that Quentin Tarantino seems to have a fascination with in films like "Django Unchained" as if we needed them emotionally to pause and digest the turmoil.',
--   10,
--   current_date
--   );


------------->Delete a film that has a review from the new_film table, what happens to the customer_review table?
--DELETE FROM new_films WHERE film_name = 'Donnie Darko'

-------------> This happens: ERROR Detail: Key (film_id)=(1) is still referenced from table "customer_review".




----------------> Exercise 2 DVD Rental
---------------->Use UPDATE to change the language of some films. Make sure that you use valid languages.
-- UPDATE film AS f
-- SET language_id = l.language_id
-- FROM language AS l
-- WHERE f.film_id = 1000
--   AND l.name = 'French';

----------------->Which foreign keys (references) are defined for the customer table? 
------------------How does this affect the way in which we INSERT into the customer table?
------------------ I do not see any foreign key there

----------------->We created a new table called customer_review. Drop this table. 
------------------Is this an easy step, or does it need extra checking?
------------------It works, I get: DROP TABLE Query returned successfully in 693 msec.

--DROP TABLE IF EXISTS customer_review;


----------------->Find out how many rentals are still outstanding 
--SELECT COUNT (*) AS outstanding_count
--FROM rental
--WHERE return_date IS NULL;

-----------------> Find the 30 most expensive movies which are outstanding 
-- SELECT f.title, MAX(p.amount) AS max_payment
-- FROM rental r
-- JOIN payment p ON r.rental_id = p.rental_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE r.return_date IS NULL
-- GROUP BY f.film_id, f.title, p.amount
-- ORDER BY p.amount DESC
-- LIMIT 30;

----------------->Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
------------------The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- SELECT f.title, f.description 
-- FROM film AS f
-- JOIN film_actor AS fa ON f.film_id = fa.film_id
-- JOIN actor AS a ON fa.actor_id = a.actor_id
-- WHERE f.description ILIKE '%sumo%'
-- 	AND a.first_name = 'Penelope'
-- 	AND a.last_name = 'Monroe'
-- LIMIT 1;
------------------The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT f.length, f.rating, f.title, fc.film_id
FROM film AS f
JOIN film_category AS fc ON fc.film_id = f.film_id
WHERE f.length < 60 AND f.rating = 'R'
ORDER BY f.title
OFFSET 1 LIMIT 1;

