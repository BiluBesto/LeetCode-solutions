class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n+1)]
        print(dp)
        for i in range(n):
            dp[i+1] = min(dp[i],dp[i-1])+cost[i]
        return min(dp[n],dp[n-1])


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna