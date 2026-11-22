class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        fq = {}
        sdup = 0
        for i in nums:
            fq[i] = fq.get(i,0)+1
            if fq[i] == 2:
                sdup = i
        for i in range(1,len(nums)+1):
            if i not in nums:
                return [sdup,i]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna