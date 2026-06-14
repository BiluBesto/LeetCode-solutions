/* Write your PL/SQL query statement below */
SELECT MAX(num) AS num
FROM (SELECT num from MyNumbers
GROUP BY num
HAVING Count(*)=1);

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna