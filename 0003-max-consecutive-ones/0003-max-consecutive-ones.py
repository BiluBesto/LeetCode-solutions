class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i]==1:
                cur+=1
            else:
                res = max(cur,res)
                cur = 0
        res = max(cur,res)
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna