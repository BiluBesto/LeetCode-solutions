class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon), len(dungeon[0])

        def isGood(initHealth):
            dp = [[0]*n for _ in range(m)]
            dp[0][0] = initHealth + dungeon[0][0]
            for r in range(m):
                for c in range(n):
                    if r>0 and dp[r-1][c]>0:
                        dp[r][c] = max(dp[r][c],dp[r-1][c] + dungeon[r][c])
                    if c>0 and dp[r][c-1]>0:
                        dp[r][c] = max(dp[r][c],dp[r][c-1]+dungeon[r][c])
            return dp[m-1][n-1]>0
        
        left = 1 
        right = 1000*(m+n) + 1
        ans = right
        while left<=right:
            mid = (left+right)//2
            if isGood(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna