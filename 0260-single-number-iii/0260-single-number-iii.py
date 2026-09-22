class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        res = []
        res.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] in res:
                res.remove(nums[i])
            else:
                res.append(nums[i])
        return res
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna