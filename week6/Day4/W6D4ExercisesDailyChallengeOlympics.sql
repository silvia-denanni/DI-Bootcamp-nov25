------------Exercise 1: Detailed Medal Analysis
------------Task 1: Identify competitors who have won at least one medal in events spanning Summer
------------and Winter Olympics. Create a temporary table to store these competitors and the
------------medal counts for each season, and then display the contents of this table.

------------Step 1: Create the temporary table
-- CREATE TEMPORARY TABLE competitor_medal_seasons (
--     competitor_id INT,
--     full_name VARCHAR(255),
--     summer_medal_count INT,
--     winter_medal_count INT
-- );

-----------Step 2: Insert competitors who won medals in both Summer and Winter Olympics, 
-----------with medal counts per season

-- INSERT INTO competitor_medal_seasons (competitor_id, full_name, summer_medal_count, winter_medal_count)
-- SELECT 
--     gc.person_id AS competitor_id,
--     p.full_name,
--     COALESCE(SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END), 0) AS summer_medal_count,
--     COALESCE(SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END), 0) AS winter_medal_count
---Count medals won in Summer games and Winter games. For each row, if the season is 'Summer',
---count 1; otherwise 0. Sum these counts to get total Summer medals. Similarly, count medals 
---for 'Winter' season. COALESCE(..., 0) ensures that if no medals are found, the count is 
---set to 0 instead of NULL.

-- FROM 
--     competitor_event ce ---------links competitors to events and medals
-- JOIN 
--     games_competitor gc ON ce.competitor_id = gc.id   ------join games_competitor(gc) to get the games each competitor participated in
-- JOIN 
--     games g ON gc.games_id = g.id   --------join games(g) to get the season of each game
-- JOIN 
--     person p ON gc.person_id = p.id --------join person (p) to get competitor names
-- WHERE 
--     ce.medal_id IS NOT NULL         ---------only count actually won medals
-- GROUP BY 
--     gc.person_id, p.full_name
-- HAVING 
--     SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) > 0
--     AND SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) > 0;
	
---------Keep only competitors who have won medals in both Summer and Winter Olympics.
---------The HAVING clause ensures the Summer medal count is more than zero and the
---------Winter medal count is more than zero.
--SELECT * FROM competitor_medal_seasons;



---------Task 2: Create a temporary table to store competitors who have won medals in exactly
---------two different sports, and then use a subquery to identify the top 3 competitors 
---------with the highest total number of medals across all sports. 
---------Display the contents of this table.

---------Step 1: Create the temporary table

-- CREATE TEMPORARY TABLE competitors_two_sports (
--     competitor_id INT,
--     full_name VARCHAR(255),
--     total_medals INT
-- );

---------Step 2: Insert competitors who won medals in exactly two different sports

-- INSERT INTO competitors_two_sports (competitor_id, full_name, total_medals)
-- SELECT 
--     gc.person_id AS competitor_id,
--     p.full_name,
--     COUNT(ce.medal_id) AS total_medals
-- FROM 
--     competitor_event ce
-- JOIN 
--     games_competitor gc ON ce.competitor_id = gc.id  -----joins competitor_event to games_competitor to get person IDs
-- JOIN 
--     event e ON ce.event_id = e.id      ----- joins event to get the sport of each event
-- JOIN 
--     person p ON gc.person_id = p.id    ----- joins person to get competitor names
-- WHERE 
--     ce.medal_id IS NOT NULL            ------ only rows where a medal was won 
-- GROUP BY 
--     gc.person_id, p.full_name          ------ group by competitor info to count total medals
-- HAVING 
--     COUNT(DISTINCT e.sport_id) = 2;    ------ only competitors who won medals in two sports

---------Step 3: Select top 3 competitors with highest total medals from the temporary table
-- SELECT *
-- FROM competitors_two_sports
-- ORDER BY total_medals DESC
-- LIMIT 3;




-------Exercise 2: Region and Competitor Performance
-------Task 1: Retrieve the regions that have competitors who have won the highest number 
-------of medals in a single Olympic event. Use a subquery to determine the event with 
-------the highest number of medals for each competitor, and then display the top 5 regions
-------with the highest total medals.

-------Step 1: Find each competitor's highest medal count in a single event
----------first CTE (competitor_event_medals) counts medals per competitor per event
----------second CTE (competitor_top_event) finds the highest medal count per competitor 
----------for any single event

-- WITH competitor_event_medals AS (              

--     SELECT 
--         ce.competitor_id,
--         ce.event_id,
--         COUNT(ce.medal_id) AS medal_count
--     FROM 
--         competitor_event ce
--     WHERE 
--         ce.medal_id IS NOT NULL
--     GROUP BY 
--         ce.competitor_id, ce.event_id
-- ),
-- competitor_top_event AS (
--     SELECT 
--         competitor_id,
--         MAX(medal_count) AS max_medals_in_event
--     FROM 
--         competitor_event_medals
--     GROUP BY 
--         competitor_id
-- )

---------Step 2: Join with regions and sum medals
-- SELECT 
--     nr.region_name,
--     SUM(cte.max_medals_in_event) AS total_top_event_medals
-- FROM 
--     competitor_top_event cte
-- JOIN 
--     games_competitor gc ON cte.competitor_id = gc.id
-- JOIN 
--     person_region pr ON gc.person_id = pr.person_id
-- JOIN 
--     noc_region nr ON pr.region_id = nr.id
-- GROUP BY 
--     nr.region_name
-- ORDER BY 
--     total_top_event_medals DESC
-- LIMIT 5;

-------For each competitor, we get their maximum medals won in any single event 
-------(competitor_top_event).
-------We join games_competitor and person_region to find the competitor's region.
-------We aggregate by region, summing each competitor's top-event medal counts.
-------Finally, we order regions by total medals and limit to top 5.



-------Task 2: Create a temporary table to store competitors who have participated in more
-------than three Olympic Games but have not won any medals. Retrieve and display the contents
-------of this table, including their full names and the number of games they participated in.

-------Step 1: Create the temporary table

-- CREATE TEMPORARY TABLE competitors_no_medals (
--     person_id INT,
--     full_name VARCHAR(255),
--     games_participated INT
-- );

-------Step 2: Insert competitors who participated in more than 3 games but won no medals

INSERT INTO competitors_no_medals (person_id, full_name, games_participated)
SELECT 
    gc.person_id,
    p.full_name,
    COUNT(DISTINCT gc.games_id) AS games_participated
FROM 
    games_competitor gc       ----join games_competitor to person to get competitor names
JOIN 
    person p ON gc.person_id = p.id
LEFT JOIN                 ----left join competitor_event filtered to only medal-winning rows (ce.medal_id IS NOT NULL) to find if the competitor won any medals
    competitor_event ce ON ce.competitor_id = gc.id AND ce.medal_id IS NOT NULL
GROUP BY                  ----group by competitor to count N distinct games they participated in and medals won
    gc.person_id, p.full_name
HAVING                       ----- filters competitors who participated in more than 3 games and have zero medals.
    COUNT(DISTINCT gc.games_id) > 3
    AND COUNT(ce.medal_id) = 0;

-----------Step 3: Display the contents of the temporary table

SELECT * FROM competitors_no_medals;
