--------------------------Exercise 1: Complex Subquery Analysis
-----------Task 1: Find the average age of competitors who have won at least one medal, 
-----------grouped by the type of medal they won. Use a correlated subquery to achieve this.

--------------------------SIMPLE QUERY
--SELECT m.medal_name,
--	AVG(gc.age) AS average_age
--FROM medal m
--JOIN games_competitor AS gc ON m.id = gc.games_id 
--GROUP BY m.medal_name;

--------------------------CORRELATED SUBQUERY
-- SELECT DISTINCT m.medal_name,
--        (SELECT AVG(gc.age)
--         FROM games_competitor gc
--         JOIN medal AS m2 ON gc.games_id = m2.id
--         WHERE m2.medal_name = m.medal_name) AS avg_age
-- FROM medal AS m
-- ORDER BY m.medal_name;

--correlated subquery calculates the average age of competitors (gc.age) who won the same medal type as the outer query's m.medal_name.
--subquery joins games_competitor and medal on competitor_id to get ages of medal winners
--No redundant joins or alias conflicts



---------Task 2: Identify the top 5 regions with the highest number of unique competitors 
---------who have participated in more than 3 different events. Use nested subqueries to filter
---------and aggregate the data.

--------------------------SIMPLE QUERY
-- SELECT nr.region_name, COUNT(DISTINCT pr.person_id) AS num_competitors
-- FROM noc_region AS nr
-- JOIN person_region AS pr ON nr.id = pr.region_id
-- JOIN competitor_event AS ce ON pr.person_id = ce.competitor_id
-- GROUP BY nr.region_name
-- HAVING COUNT(DISTINCT ce.event_id) > 3
-- ORDER BY num_competitors DESC
-- LIMIT 5;

--------------------------NESTED SUBQUERY 
-- SELECT nr.region_name, region_competitor_counts.num_competitors
-- FROM noc_region AS nr
-- JOIN (
--     SELECT pr.region_id, COUNT(DISTINCT pr.person_id) AS num_competitors
--     FROM person_region pr
--     WHERE pr.person_id IN (
--         SELECT ce.competitor_id
--         FROM competitor_event AS ce
--         GROUP BY ce.competitor_id
--         HAVING COUNT(DISTINCT ce.event_id) > 3
--     )
--     GROUP BY pr.region_id
-- ) AS region_competitor_counts ON nr.id = region_competitor_counts.region_id
-- ORDER BY region_competitor_counts.num_competitors DESC
-- LIMIT 5;

--Inner subquery (in WHERE pr.person_id IN (...) finds competitors (person_id) who participated in more than 3 distinct events
--Middle subquery (region_competitor_counts) counts unique competitors per region, filtering only those who passed the inner subquery condition.
-- Outer query joins region info (noc_region) to get region names, orders by number of competitors descending and limits to top 5 regions.



---------Task 3: Create a temporary table to store the total number of medals won by each 
---------competitor and filter to show only those who have won more than 2 medals. 
---------Use subqueries to aggregate the data.

-- Step 1: Create temporary table with total medals per competitor
-- CREATE TEMPORARY TABLE tot_competitor_medals AS
-- SELECT 
--     ce.competitor_id,
--     COUNT(*) AS medal_number
-- FROM 
--     competitor_event ce
-- WHERE 
--     ce.medal_id IS NOT NULL  -- Only count actual medals won
-- GROUP BY 
--     ce.competitor_id;

-- -- Step 2: Select competitors with more than 2 medals
-- SELECT *
-- FROM tot_competitor_medals
-- WHERE medal_number > 2;

----------aggregation (COUNT + GROUP BY) to summarize medals per competitor.
----------subquery-like structure by creating a temporary table for intermediate results.
----------separates data preparation (temp table) and filtering (final select).



---------Task 4: Use a subquery within a DELETE statement to remove records of competitors 
---------who have not won any medals from a temporary table created for analysis.
---------Step 1: Create temporary table with total medals per competitor
-- CREATE TEMPORARY TABLE competitor_medal_counts AS
-- SELECT 
--     ce.competitor_id,
--     COUNT(*) AS medal_number
-- FROM 
--     competitor_event AS ce
-- WHERE 
--     ce.medal_id IS NOT NULL  -- Only count rows where a medal was actually won
-- GROUP BY 
--     ce.competitor_id;

---------Step 2: Select competitors with more than 2 medals
-- SELECT *
-- FROM competitor_medal_counts
-- WHERE medal_number > 2;

---------Count medals per competitor by grouping on competitor_id.
---------Filter out rows where medal_id is NULL (meaning no medal won in that event).
---------Temporary table stores this aggregated data.
-- Then you can query or filter this table as needed.

-- DELETE FROM competitor_medal_counts
-- WHERE medal_number <= 2;


----------Exercise 2: Advanced Data Manipulation and Optimization
----------Task 1: Update the heights of competitors based on the average height of competitors
----------from the same region. Use a correlated subquery within the UPDATE statement.
-- UPDATE person p_outer
-- SET height = (
--     SELECT AVG(p_inner.height)
--     FROM person p_inner
--     JOIN person_region pr_inner ON p_inner.id = pr_inner.person_id
--     WHERE pr_inner.region_id = (
--         SELECT pr_outer.region_id
--         FROM person_region pr_outer
--         WHERE pr_outer.person_id = p_outer.id
--         LIMIT 1
--     )
-- );

-- For each row in person (aliased as p_outer), the subquery:
-- Finds the region_id of that person from person_region (pr_outer).
-- Then calculates the average height of all persons (p_inner) in that same region (pr_inner.region_id = pr_outer.region_id).
-- The LIMIT 1 ensures the subquery returns a single region_id if a person belongs to multiple regions (adjust if your data model forbids multiple regions per person).
-- The outer UPDATE sets the person height to that average.

---------------------BUT THIS QUERY IS TOO COMPUTATIONALLY EXPENSIVE!---------------------
---------------------Optimized approach: JOIN  with a derived table ---------------------
-- WITH avg_height_per_region AS (
--     SELECT 
--         pr.region_id,
--         AVG(p.height) AS avg_height
--     FROM 
--         person p
--     JOIN 
--         person_region pr ON p.id = pr.person_id
--     GROUP BY 
--         pr.region_id
-- )
-- UPDATE person p
-- SET height = a.avg_height
-- FROM avg_height_per_region a, person_region pr
-- WHERE pr.person_id = p.id
--   AND pr.region_id = a.region_id;

-----------------Using a CTE to pre-aggregate:---------------------
--Calculating the average height per region once (in the CTE) is efficient. 
--It avoids recalculating the average repeatedly for each person, which would be very slow.
-----------------Joining tables to relate persons to regions---------------------
-- Since the person table doesn’t directly store region info, the query joins person_region
--to find each person’s region.
-----------------Avoiding referencing the target table in the FROM clause---------------------
-- In PostgreSQL, when updating a table, you cannot include that same table in the FROM clause. 
-- Instead, you join related tables and use the WHERE clause to match rows. 
--This ensures the database knows which rows to update and what values to assign.



----------Task 2:  Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. 
----------Use nested subqueries for filtering.
----------Step 1: Create the temporary table
-- CREATE TEMPORARY TABLE competitor_multiple_events (
--     competitor_id INT,
--     games_id INT,
--     total_events INT
-- );
-- ---------Step 2: Insert data using nested subqueries
-- INSERT INTO competitor_multiple_events (competitor_id, games_id, total_events)
-- SELECT competitor_id, games_id, total_events FROM (
--     SELECT 
--         ce.competitor_id,
--         gc.games_id,
--         COUNT(*) AS total_events
--     FROM 
--         competitor_event ce
--     JOIN 
--         games_competitor gc ON ce.competitor_id = gc.id
--     GROUP BY 
--         ce.competitor_id, gc.games_id
-- ) AS sub
-- WHERE total_events > 1;

---The nested subquery sub aggregates events per competitor per game, and the outer query filters those with more than one event.


----------Task 3:Identify regions where the average number of medals won per competitor 
--------is greater than the overall average. Use subqueries to calculate and compare averages.

-------------------Approach:--------------------------------- 
--Calculate average medals per competitor per region
-- For each region, find the total medals won by all competitors in that region, divided by the number of competitors in that region.
-- Calculate overall average medals per competitor
-- Across all competitors (all regions), calculate the average medals per competitor.
-- Select regions where regional average > overall average
SELECT 
    nr.region_name,
    region_medals.avg_medals_per_competitor
FROM 
    noc_region nr
JOIN (
    -- Average medals per competitor per region
    SELECT 
        pr.region_id,
        AVG(medal_counts.medal_count) AS avg_medals_per_competitor
    FROM 
        person_region pr
    JOIN (
        -- Count medals per competitor
        SELECT 
            ce.competitor_id,
            COUNT(ce.medal_id) AS medal_count
        FROM 
            competitor_event ce
        WHERE 
            ce.medal_id IS NOT NULL
        GROUP BY 
            ce.competitor_id
    ) AS medal_counts ON medal_counts.competitor_id = pr.person_id
    GROUP BY 
        pr.region_id
) AS region_medals ON region_medals.region_id = nr.id
WHERE 
    region_medals.avg_medals_per_competitor > (
        -- Overall average medals per competitor
        SELECT 
            AVG(medal_count)
        FROM (
            SELECT 
                ce.competitor_id,
                COUNT(ce.medal_id) AS medal_count
            FROM 
                competitor_event ce
            WHERE 
                ce.medal_id IS NOT NULL
            GROUP BY 
                ce.competitor_id
        ) AS overall_medals
    );

-- The innermost subquery (medal_counts) counts medals per competitor.
-- The middle subquery joins person_region to assign competitors to regions and calculates the average medals per competitor per region.
-- The outer query joins with noc_region to get region names.
-- The WHERE clause compares each region's average medals per competitor to the overall average medals per competitor (calculated by another subquery).
-- Only regions with an average above the overall average are returned.