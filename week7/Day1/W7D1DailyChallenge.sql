-- Create the employees table
-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     employee_name VARCHAR(50),
--     salary DECIMAL(10, 2),
--     hire_date VARCHAR(20),
--     department VARCHAR(50)
-- );

-- Insert 20 sample records 
-- INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
-- (1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
-- (2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
-- (3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
-- (4, 'John White', 90000.00, '2020-11-05', 'Finance'),
-- (5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
-- (6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
-- (7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
-- (8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
-- (9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
-- (10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
-- (11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
-- (12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
-- (13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
-- (14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
-- (15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
-- (16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
-- (17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
-- (18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
-- (19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
-- (20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

------------------------------------------------------------------------------------------------
--------------------0) Create backup
-- CREATE TABLE employees_backup AS
-- SELECT *
-- FROM employees;


--------------------1) Identify and handle any missing value
-- SELECT *
-- FROM employees
-- WHERE department IS NULL

-- UPDATE employees
-- SET department = 'Unknown'      ---------updating with an ad hoc string value (non numeric column)
-- WHERE department IS NULL

-- SELECT * FROM employees


--------------------2)Check for and eliminate any duplicate rows in the dataset.
-------------------- find duplicates by grouping on all columns except pk ( all columns if no pk)
---------------------For rows appearing more than once:

-- SELECT employee_name, salary, hire_date, department, COUNT (*)
-- FROM employees
-- GROUP BY employee_name, salary, hire_date, department  -------grouping on all columns EXCEPT pk
-- HAVING COUNT (*) > 1                -------------- HAVING COUNT ALWAYS after GROUP BY!


---------------------There are NO DUPLICATED ROWS here, in case there were, use ROW_NUMBER():
---------------------it assigns a unique number to each row within the partition of the 
---------------------specified column. Rows with a number greater than 1 are considered 
---------------------duplicates and are deleted.
-- WITH CTE AS (
--     SELECT 
--         employee_id,
--         ROW_NUMBER() OVER (
--             PARTITION BY employee_name, salary, hire_date, department
--             ORDER BY employee_id
--         ) AS rn
--     FROM employees
-- )
-- DELETE FROM employees
-- WHERE employee_id IN (
--     SELECT employee_id FROM CTE WHERE rn > 1
-- );


--------------------3) Correct any structural issues, such as inconsistent naming conventions 
---------------------- or formatting errors.
-- SELECT INITCAP(employee_name) AS capitalized_name
-- FROM employees;



--------------------4) Ensure all columns have appropriate data types (e.g. the hire_date column).

--SELECT CAST(hire_date AS DATE) FROM employees

--------------------5)Detect and address any outliers that may skew the analysis.
--------------------Creating CTE 
-- WITH salary_stats AS (
--     SELECT
--         PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS Q1,
--         PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS Q3
--     FROM employees
-- ),
-- salary_bounds AS (
--     SELECT
--         Q1,
--         Q3,
--         (Q3 - Q1) AS IQR,        ---(IQR) measures the spread of the middle 50% of salaries 
--         (Q1 - 1.5 * (Q3 - Q1)) AS lower_bound,   ----salary below this is unusually low
--         (Q3 + 1.5 * (Q3 - Q1)) AS upper_bound    ----salary above this is unusually high
--     FROM salary_stats
-- )
-- SELECT e.*           ----all columns (*) from the employees table (e)
-- FROM employees AS e, salary_bounds AS sb
-- WHERE e.salary < sb.lower_bound OR e.salary > sb.upper_bound;

------------In this case there are NO OUTLIERS, but if there were, we have two options:

------------a)Remove outliers:

-- DELETE FROM employees
-- WHERE salary < (SELECT lower_bound FROM salary_bounds)
--    OR salary > (SELECT upper_bound FROM salary_bounds);

-----------b)Cap outliers by replacing extreme values with the nearest boundary

-- UPDATE employees
-- SET salary = CASE
--     WHEN salary < (SELECT lower_bound FROM salary_bounds) THEN (SELECT lower_bound FROM salary_bounds)
--     WHEN salary > (SELECT upper_bound FROM salary_bounds) THEN (SELECT upper_bound FROM salary_bounds)
--     ELSE salary
-- END;



--------------------5)Standardize and normalize data where applicable to ensure consistency.
-----------a) standardize salary --> (salary - mean) / stddev
-- WITH stats AS (
--     SELECT 
--         AVG(salary) AS mean_salary,
--         STDDEV(salary) AS stddev_salary
--     FROM employees
-- )
--------compute standardized salary for each employee
-- SELECT 
--     employee_id,
--     employee_name,
--     (salary - stats.mean_salary) / stats.stddev_salary AS standardized_salary,
--     hire_date,
--     department
-- FROM employees, stats;

-----------b) normalize salary (MIN-MAX) ---> (salary - min) / (max - min)
-- WITH stats AS (
--     SELECT 
--         MIN(salary) AS min_salary,
--         MAX(salary) AS max_salary
--     FROM employees
-- )
-- SELECT 
--     employee_id,
--     employee_name,             ---NULLIF prevents division by 0 if all salaries are the same
--     (salary - stats.min_salary) / NULLIF((stats.max_salary - stats.min_salary), 0) AS normalized_salary,
--     hire_date,
--     department
-- FROM employees, stats;

-------------Add new standardized_salary and normalized_salary columns
-- ALTER TABLE employees
-- ADD COLUMN standardized_salary DECIMAL(10, 4),
-- ADD COLUMN normalized_salary DECIMAL(10, 4);

-- WITH stats AS (
--     SELECT 
--         AVG(salary) AS mean_salary,
--         STDDEV(salary) AS stddev_salary,
--         MIN(salary) AS min_salary,
--         MAX(salary) AS max_salary
--     FROM employees
-- )
-- UPDATE employees
-- SET 
--     standardized_salary = (salary - (SELECT mean_salary FROM stats)) / NULLIF((SELECT stddev_salary FROM stats), 0),
--     normalized_salary = (salary - (SELECT min_salary FROM stats)) / NULLIF((SELECT max_salary FROM stats) - (SELECT min_salary FROM stats), 0)

SELECT employee_id, salary, standardized_salary, normalized_salary
FROM employees
ORDER BY employee_id