class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hasmap = {}
        maxlen = 0
        for num in nums:
            hasmap[num] = 1+hasmap.get(num,0)
        for num in hasmap:
            if num+1 in hasmap:
                curlen = hasmap[num] + hasmap[num+1]
                maxlen = max(maxlen,curlen)
        return maxlen

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna