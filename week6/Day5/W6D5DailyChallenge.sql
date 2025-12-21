------------Task 1: Calculate the Average Budget Growth Rate for Each Production Company
------------Calculate the average budget growth rate for each production company across all movies
------------they have produced. Use window functions to determine the budget growth rate and then 
------------calculate the average growth rate.


-- SELECT movies.movie.budget, movies.movie.movie_id,
--        movies.production_company.company_id, movies.production_company.company_name
-- 	   movies.movie_company_movie_id, movies.movie_company_company_id

-------STEP 1: CTE to calculate movie_budgets per production company, joining tables 'movie',
-------'production_company' and 'movie_company'
-- WITH movie_budgets AS (
--     SELECT
--         mc.company_id,
--         pc.company_name,
--         mc.movie_id,
--         m.budget
--     FROM movies.movie_company AS mc
--     JOIN movies.movie AS m ON mc.movie_id = m.movie_id
--     JOIN movies.production_company AS pc ON mc.company_id = pc.company_id
-- ),
-------STEP 2: CTE to calculate budget_growth per production company (budget change from 
-------one movie to the nex)
-- budget_growth AS (
--     SELECT
--         company_id,
--         company_name,
--         movie_id,
--         budget,
-- -------looking at previous row budget when we order movies by ID within each company:		
--         LAG(budget) OVER (PARTITION BY company_id ORDER BY movie_id) AS prev_budget,
-- -------calculating % change in budget compared to the previous movie (budget_growth_rate):	
--         CASE 
--             WHEN LAG(budget) OVER (PARTITION BY company_id ORDER BY movie_id) IS NULL THEN NULL
--             WHEN LAG(budget) OVER (PARTITION BY company_id ORDER BY movie_id) = 0 THEN NULL
-- 			ELSE (budget - LAG(budget) OVER (PARTITION BY company_id ORDER BY movie_id)) / LAG(budget) OVER (PARTITION BY company_id ORDER BY movie_id)
--         END AS budget_growth_rate
--     FROM movie_budgets
-- )
-- SELECT
--     company_id,
--     company_name,
--     AVG(budget_growth_rate) AS avg_budget_growth_rate  --- how much company budgets tend to grow on average from one movie to the next
-- ORDER BY avg_budget_growth_rate DESC; ---sorts companies so the ones with the highest average growth rate come first
-- FROM budget_growth
-- WHERE budget_growth_rate IS NOT NULL
-- GROUP BY company_id, company_name   --- groups the movies by each company 

-------------Further explanation: 
-------------CASE WHEN LAG.....:if there is no previous movie (as in first movie for a company),
-------------or previous budget was 0, no growth calculation (NULL to say “no data”).
-------------ELSE.....:subtract the previous budget from the current budget, then 
-------------divide by the previous budget to get decimal growth rate (0.2 means 20% growth)

--------------------------------------------------------------------------------------------------------

-------------Task 2: Determine the Most Consistently High-Rated Actor
-------------Identify the actor who has appeared in the most movies that are rated above 
-------------the average rating of all movies. Use window functions and CTEs to calculate
-------------the average rating and filter the actors based on this criterion.


-------------STEP 1: calculate the overall average of the vote_average column in movie table 
-------------with CTE --->movie ratings on avg are 6.10 (single value)
-- WITH avg_movie_rating AS (
-- 	SELECT AVG(movie.vote_average) AS avg_rating
-- 	FROM movies.movie)
-- ,
-------------STEP 2: identify movies rated above this average ----> 1000/2756 movies
-- above_avg_movie_rating AS (
-- 	SELECT movie.movie_id, movie.vote_average	
-- 	FROM movies.movie, avg_movie_rating   -----include avg_movie_rating in FROM clause of CTE 2 as a CONSTANT to make the average rating available for comparison
-- 	WHERE vote_average > avg_movie_rating.avg_rating)
-- ,	   
-------------STEP 3/4: find actors who appeared in these higher-rated movies and count 
-------------how many such movies each actor appeared in
-- actor_high_rated_counts AS (
--     SELECT 
--         mc.person_id,
--         COUNT(*) AS high_rated_movie_count
--     FROM movies.movie_cast mc
--     JOIN above_avg_movie_rating a ON mc.movie_id = a.movie_id
--     GROUP BY mc.person_id)
-- ,
-------------STEP 5: rank actors by their count of high-rated movies
-- ranked_actors AS (
--     SELECT 
--         person_id,
--         high_rated_movie_count,
--         RANK() OVER (ORDER BY high_rated_movie_count DESC) AS rank
--     FROM actor_high_rated_counts
-- )
-- -------------STEP 6: select the top-ranked actor with their name and count
-- SELECT 
--     p.person_name,
--     r.high_rated_movie_count
-- FROM ranked_actors r
-- JOIN movies.person p ON r.person_id = p.person_id
-- WHERE r.rank = 1


-------------Task 3: Calculate the Rolling Average Revenue for Each Genre
-------------Calculate the rolling average revenue for movies within each genre, considering 
-------------only the last three movies released in the genre. 
-------------Use window functions with the ROWS frame specification to achieve this.

SELECT
    g.genre_name,
    mg.movie_id,
    m.revenue,
-------------Calculate rolling average revenue over the current and previous 2 movies in the genre
    AVG(m.revenue) OVER (
        PARTITION BY mg.genre_id
        ORDER BY mg.movie_id
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_revenue_last_3
FROM movies.movie_genres mg
JOIN movies.movie m ON mg.movie_id = m.movie_id
JOIN movies.genre g ON mg.genre_id = g.genre_id
ORDER BY g.genre_name, mg.movie_id;

	   
	   