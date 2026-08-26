class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i]=-nums[i]
                k-=1
        nums = sorted(nums)
        if k>0 and k%2!=0:
            nums[0] = -nums[0]
        return sum(nums)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna