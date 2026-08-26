class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += grid[i][j]*6

                    area -= (grid[i][j] - 1 ) *2
                
                    if i+1<n:
                        area -= 2 * min(grid[i][j],grid[i+1][j])
                    if j+1<n:
                        area -=2 * min(grid[i][j],grid[i][j+1])
        return area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna