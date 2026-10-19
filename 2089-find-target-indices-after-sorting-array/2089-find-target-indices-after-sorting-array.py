class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna