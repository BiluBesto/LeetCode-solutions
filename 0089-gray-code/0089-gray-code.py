class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(0,2**n):
            res.append(i^(i//2))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna