class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(n)] for _ in range(k+1)]
        
        for i in range(1,k+1):
            best = -prices[0]
            for j in range(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j]+best)
                best = max(best,dp[i-1][j]-prices[j])

        return dp[k][n-1]
#dp[2][5]=max(dp[1][4],dp[1][3]+p[5]-p[4],dp[1][2]+p[5]-p[3])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna