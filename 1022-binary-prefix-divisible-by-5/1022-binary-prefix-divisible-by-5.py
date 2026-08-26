class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        val = 0 
        for i in range(len(nums)):
            val = ((val<<1) + nums[i])%5
            nums[i]= val==0
        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna