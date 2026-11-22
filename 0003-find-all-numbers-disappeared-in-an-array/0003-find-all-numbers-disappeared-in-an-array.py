class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        fq = {}
        res = []
        for i in nums:
            fq[i] = fq.get(i,0)+1
        for i in range(1,len(nums)+1):
            if i not in fq:
                res.append(i)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna