class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        max_count = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>prev:
                count+=1
                prev = nums[i]
                max_count = max(max_count,count)
            else:
                count = 1
                prev = nums[i]
        return max_count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna