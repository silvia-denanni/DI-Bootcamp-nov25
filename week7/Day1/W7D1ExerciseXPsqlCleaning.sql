-- -- Exercise 1: Building a Comprehensive Dataset for Employee Analysis
-- -- Create a temporary table that join all tables and create a new one using LEFT JOIN.
-- -- Create an unique identifier code between the columns ‘employee_id’ and ‘date’ and call it ‘id’.
-- -- Convert the column ‘date’ to DATE type because it was previously configured as TIMESTAMP.
-- -- Transform this new table into a dataset “df_employee” for analysis.

-- CREATE TEMPORARY TABLE df_employee AS
-- SELECT 
--     -- Unique identifier combining employee_id and date as text
--     s.employee_id || '_' || TO_CHAR(s.date, 'YYYY-MM-DD') AS id,
    
--     -- Convert timestamp to date (only date part)
--     DATE(s.date) AS month_year,
    
--     -- Columns from salaries table
--     s.employee_id,
--     s.employee_name,
--     s.salary,
--     s.comp_code,
--     s.comp_name,
--     s.func_code,
--     s.func,
    
--     -- Columns from functions table
--     f.function_group,
    
--     -- Columns from employee table
--     e.employee_code_emp,
--     e.employee_name_emp,
--     e.gender_mf AS gender,
--     e.age,
    
--     -- Columns from company table
--     c.company_city,
--     c.company_state,
--     c.company_type,
--     c.const_site_category

-- FROM salaries AS s
-- LEFT JOIN functions AS f ON s.func_code = f.function_code
-- LEFT JOIN employee AS e ON s.comp_code = e.comp_code_emp AND s.employee_id = e.employee_code_emp
-- LEFT JOIN company AS c ON s.comp_name = c.company_name;


-- -- Exercise 2: Cleaning Data for Consistency and Quality
-- -- 1. run the following SQLite request and observe your new table.

-- select * FROM df_employee

-- -- 2. Remove all unwanted spaces from all text columns using TRIM

-- UPDATE df_employee
-- SET
-- id = TRIM(id),
-- comp_code = TRIM(comp_code),
-- comp_name = TRIM(comp_name),
-- func = TRIM(func),
-- function_group = TRIM(function_group),
-- gender = TRIM(gender),
-- company_city = TRIM(company_city),
-- company_state = TRIM(company_state),
-- company_type = TRIM(company_type),
-- const_site_category = TRIM(const_site_category)


-- -- 3. Check for NULL values and empty values.

-- SELECT *
-- FROM df_employee
-- WHERE id IS NULL OR id = ''
--    OR month_year IS NULL
--    OR employee_id IS NULL  -- no = '' here because employee_id is integer
--    OR comp_code IS NULL    -- assuming comp_code is integer, no = ''
--    OR comp_name IS NULL OR comp_name = ''
--    OR func IS NULL OR func = ''
--    OR function_group IS NULL OR function_group = ''
--    OR gender IS NULL OR function_group = ''
--    OR company_city IS NULL OR company_city = ''
--    OR company_state IS NULL OR company_state = ''
--    OR const_site_category IS NULL OR const_site_category = '';


-- --4. Delete rows of the detected missing values.

-- DELETE FROM df_employee
-- WHERE salary IS NULL
--    OR id = ' ' OR id IS NULL
--    OR month_year IS NULL
--    OR employee_id IS NULL
--    OR comp_code IS NULL
--    OR comp_name = ' ' OR comp_name IS NULL
--    OR func = ' ' OR func IS NULL
--    OR function_group = ' ' OR function_group IS NULL
--    OR gender IS NULL
--    OR company_city = ' ' OR company_city IS NULL
--    OR company_state = ' ' OR company_state IS NULL
--    OR const_site_category = ' ' OR const_site_category IS NULL;

--  SELECT * FROM df_employee


-- -- Exercise 3 : Calculating Current Employee Counts by Company
-- -- How many employees do the companies have today?
-- -- Group them by company

-- SELECT comp_name, COUNT(DISTINCT employee_id) AS employee_count
-- FROM salaries
-- GROUP BY comp_name


-- -- Exercise 4 : Analyzing Employee Distribution by City and Over Time
-- -- What is the total number of employees each city? Add a percentage column

SELECT 
	c.company_city, 
	COUNT(DISTINCT s.employee_id) AS employee_count,  ---returns the count per group
	ROUND(
      COUNT(DISTINCT s.employee_id) * 100.0 / SUM(COUNT(DISTINCT s.employee_id)) OVER (), 
      2
    ) AS employee_percentage  -------Take the counts from all cities, SUM them up OVER the entire result set - () mean no partitioning, so over all rows.
FROM company AS c
JOIN salaries AS s ON c.company_name = s.comp_name
GROUP BY company_city;


-- -- What is the total number of employees each month?

SELECT 
    DATE_TRUNC('month', date) AS month_year,  -- Extract the month and year from the date
    COUNT(DISTINCT employee_id) AS total_employees
FROM salaries  
GROUP BY month_year
ORDER BY month_year; 

-- -- What is the average number of employees each month?

SELECT 
    DATE_TRUNC('month', date) AS month_year,  -- Extract the month and year from the date
    AVG(DISTINCT employee_id) AS total_employees
FROM salaries  
GROUP BY month_year
ORDER BY month_year; 


-- -- Exercise 5: Analyzing Employment Trends and Salary Metrics
-- -- What is the minimum and maximum number of employees throughout all the months? 
-- -- In which months were they?

SELECT 
    DATE_TRUNC('month', date) AS month_year,  -- Extract the month and year from the date
    MIN(DISTINCT employee_id) AS min_employees,
	MAX(DISTINCT employee_id) AS max_employees
	
FROM salaries  
GROUP BY month_year
ORDER BY month_year; 

-- -- What is the monthly average number of employees by function group?
WITH monthly_counts AS (      ----calculates distinct employee number per month and function group
    SELECT 
        DATE_TRUNC('month', s.date) AS month_year,
        f.function_group,
        COUNT(DISTINCT s.employee_id) AS employee_count
    FROM salaries AS s
    JOIN functions AS f ON s.func_code = f.function_code
    GROUP BY month_year, f.function_group
)
SELECT 
    function_group,
    ROUND(AVG(employee_count)::numeric, 2) AS avg_employees_per_month   ---''::numeric' casts the average to numeric for rounding
FROM monthly_counts
GROUP BY function_group
ORDER BY function_group;       ---calculates AVG of monthly counts per function group


-- -- What is the annual average salary?
