class Solution:
    def allCellsDistOrder(self, m: int, n: int, i: int, j: int) -> List[List[int]]:
        return sorted(product(range(m),range(n)), key = lambda p:(abs(p[0]-i)+abs(p[1]-j)))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna