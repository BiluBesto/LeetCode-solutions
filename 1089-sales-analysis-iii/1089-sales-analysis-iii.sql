# Write your MySQL query statement below
SELECT product_id , product_name from Product
WHERE product_id IN(select product_id from sales
group by product_id having min(sale_date)>='2019-01-01'
AND max(sale_date)<='2019-03-31')

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna