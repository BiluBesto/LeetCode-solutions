class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = [-1]*(n)
        dp[0] = 0    
        for i in range(1,n):
            for j in range(i):
                if abs(nums[i]-nums[j]) <= target and dp[j] != -1:
                    dp[i] = max(dp[i],dp[j]+1)
        return dp[-1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna