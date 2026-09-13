CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    SELECT DISTINCT salary INTO result FROM (SELECT salary, DENSE_RANK() OVER(ORDER BY Salary DESC) R FROM Employee) WHERE R = N;
    RETURN result;
    EXCEPTION
        WHEN OTHERS THEN
            RETURN NULL;
END;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna