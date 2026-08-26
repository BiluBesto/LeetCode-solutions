class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        res1,res2 = True,True
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:
                continue
            else:
                res1= False
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                continue
            else:
                res2 = False

        return res1 or res2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna