class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [ i^(i>>1) for i in range(2**n)]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna