/* Write your PL/SQL query statement below */
Select p.product_name product_name,s.year year, s.price price from 
Sales s 
JOIN Product p 
ON s.product_id = p.product_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna