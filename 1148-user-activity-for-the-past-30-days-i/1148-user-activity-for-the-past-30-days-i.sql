/* Write your PL/SQL query statement below */
SELECT TO_CHAR(activity_date,'YYYY-MM-DD') as day, COUNT(distinct user_id) as active_users
from activity where activity_date between '2019-06-28' and '2019-07-27'
GROUP BY activity_date

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna