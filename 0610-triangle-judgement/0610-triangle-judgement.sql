/* Write your PL/SQL query statement below */
SELECT x,y,z ,
CASE WHEN 
x+y>z and x+z>y and y+z>x THEN 'Yes'
ELSE 'No' END triangle
FROM Triangle;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna