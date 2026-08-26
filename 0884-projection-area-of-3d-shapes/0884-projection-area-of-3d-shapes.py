class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xa = sum(1 for row in grid for val in row if val > 0)
        ya = sum(max(row) for row in grid)
        za = sum(max(col) for col in zip(*grid))

        return xa + za + ya

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna