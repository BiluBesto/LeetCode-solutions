class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1!=h2 for h1,h2 in zip(heights,sorted(heights)))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna