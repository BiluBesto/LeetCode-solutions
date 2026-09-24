class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        for i in range(len(nums)):
            if i==0:
                left.append(0)
                continue
            cur = 0
            for j in range(0,i):
                cur+=nums[j]
            left.append(cur)
        for i in range(len(nums)):
            if i == len(nums)-1:
                right.append(0)
                continue
            cur = 0
            for j in range(i+1,len(nums)):
                cur+=nums[j]
            right.append(cur)
        i = 0
        res = []
        while i < len(left):
            res.append(abs(left[i]-right[i]))
            i+=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna