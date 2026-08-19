class Solution:
    @cache
    def uniquePaths(self, m: int, n: int,i=0,j=0) -> int:
        
        if i>=m or j>=n:
            return 0
        if i==m-1 or j==n-1:
            return 1
        return self.uniquePaths(m,n,i+1,j) + self.uniquePaths(m,n,i,j+1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna