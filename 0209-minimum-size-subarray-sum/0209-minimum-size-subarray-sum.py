class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        j=0
        minl = float('inf')
        prefSum = [0]
        for i in range(len(nums)):
            prefSum.append(prefSum[i]+nums[i])
        i=0
        print(prefSum)
        while i<len(nums) and j<len(nums):
            curr = prefSum[j+1] - prefSum[i]
            if curr>=target:
                minl = min(minl,j-i+1)
                i+=1
            else:
                j+=1
        return 0 if minl == float('inf') else minl

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna