/* Write your PL/SQL query statement below */
SELECT customer_number from ( 
    SELECT customer_number, ROW_NUMBER() OVER ( order by count(*) desc ) rn from orders
    group by customer_number
)
where rn = 1

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna