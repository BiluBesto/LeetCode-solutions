/* Write your PL/SQL query statement below */
SELECT d.name Department, e.name Employee, e.salary  Salary
FROM Employee e
JOIN Department d
ON e.departmentId = d.id
WHERE (e.departmentId,e.salary) IN (
    SELECT departmentId, MAX(salary) 
    FROM Employee 
    GROUP BY departmentId;
);

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna