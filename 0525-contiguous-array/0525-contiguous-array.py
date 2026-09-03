class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sumv = 0
        maxl = 0
        for i, num in enumerate(nums):
            sumv+= 1 if num==1 else -1
            if sumv == 0:
                maxl = i+1
            elif sumv in mp:
                maxl = max(maxl,i-mp[sumv])
            else:
                mp[sumv]=i
        return maxl

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna