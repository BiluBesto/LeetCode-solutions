class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted(x*x for x in nums)

        k = len(nums)//2

        return sum(a[k:]) - sum(a[:k])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna