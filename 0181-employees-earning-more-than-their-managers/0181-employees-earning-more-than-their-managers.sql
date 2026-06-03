/* Write your PL/SQL query statement below */
SELECT e1.name Employee 
FROM Employee e1
JOIN Employee e2
ON e1.managerId = e2.id
WHERE e1.salary>e2.salary and e1.managerId =  e2.id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna