class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0 
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[left],nums[i] = nums[i],nums[left]
                left+=1
        return nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna