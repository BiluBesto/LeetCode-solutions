class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first , count , res , degree = {},{},0,0
        for i , a in enumerate(nums):
            first.setdefault(a,i)
            count[a]=count.get(a,0)+1
            if count[a]>degree:
                degree = count[a]
                res = i - first[a] + 1
            elif count[a] == degree:
                res = min(res,i-first[a]+1)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna