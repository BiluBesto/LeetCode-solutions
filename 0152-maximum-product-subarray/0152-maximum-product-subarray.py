class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmax = curmin = 1

        for i in range(len(nums)):
            temp = curmax * nums[i]
            curmax = max(temp,curmin*nums[i],nums[i])
            curmin = min(temp,curmin*nums[i],nums[i])

            res = max(res,curmax)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna