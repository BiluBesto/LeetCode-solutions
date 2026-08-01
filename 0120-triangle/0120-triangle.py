class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        memo = triangle[rows-1].copy()
        for i in range(rows-2,-1,-1):
            for j in range(i+1):
                memo[j] = min(memo[j],memo[j+1]) + triangle[i][j]
        return memo[0]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna