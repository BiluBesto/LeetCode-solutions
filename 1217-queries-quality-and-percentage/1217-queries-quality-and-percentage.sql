# Write your MySQL query statement below
SELECt query_name, round(avg(cast(rating as decimal)/position),2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*),2) as poor_query_percentage
from queries group by query_name

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna