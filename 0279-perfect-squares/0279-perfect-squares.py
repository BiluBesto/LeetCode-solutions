class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n+1]*(n+1)
        dp[0]=0
        
        for i in range(1,n+1):
            j = 1
            while j*j<=i:
                dp[i]=min(dp[i],1+dp[i-j*j])
                j+=1
        return dp[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna