suf = [0]*100
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suf[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suf[i] = min(suf[i+1],nums[i])
        mx = 0
        for i in range(n):
            mx = max(mx,nums[i])
            if mx-suf[i] <= k:
                return i
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna