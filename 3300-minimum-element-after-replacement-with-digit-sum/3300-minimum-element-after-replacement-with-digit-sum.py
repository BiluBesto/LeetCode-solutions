class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            res.append(sum([int(x)for x in str(i)]))
        return min(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna