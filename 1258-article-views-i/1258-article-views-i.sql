/* Write your PL/SQL query statement below */
SELECT distinct author_id as ID 
from Views
WHERE author_id = viewer_id
order by author_id asc;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna