class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        #l and r indicate the no of elements range for the subarray 
        #the subararay sum, greater than 0, return min(sumsubarr>0),else return -1

        res = float('inf')

        for i in range(l,r+1):
            cur = sum(nums[0:i])
            if cur>0:
                res = min(res,cur)
            for j in range(1,len(nums)-i+1):
                cur += (nums[j+i-1] - nums[j-1])
                if cur>0:
                    res = min(res,cur)

        return res if res!=float('inf') else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna