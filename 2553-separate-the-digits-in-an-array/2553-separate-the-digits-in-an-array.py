class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            res.extend([int(x) for x in str(i)])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna