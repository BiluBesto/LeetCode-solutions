class Solution:
    def uniquePaths(self, m: int, n: int,i=0,j=0) -> int:
        dp=[[1]*n for _ in range(m)]
        for i,j in product(range(1,m),range(1,n)):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna