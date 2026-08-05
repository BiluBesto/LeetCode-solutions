class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cursum=0
        maxva = float('-inf')
        for i in range(k):
            cursum+=nums[i]
        maxva=max(cursum,maxva)
        for i in range(k,len(nums)):
            cursum-=nums[i-k]
            cursum+=nums[i]
            maxva=max(cursum,maxva)
        return maxva/k

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna