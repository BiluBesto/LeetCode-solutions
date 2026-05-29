/* Write your PL/SQL query statement below */
SELECT d.name Department, e.name Employee, e.salary Salary
FROM Employee e
JOIN Department d
ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId 
    AND e2.salary > e.salary;
) < 3;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna