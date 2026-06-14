/* Write your PL/SQL query statement below */
SELECT e.name, b.bonus 
from Employee e 
LEFT JOIN 
Bonus b 
ON e.empID = b.empID
where b.bonus<1000 or b.bonus is NULL


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna