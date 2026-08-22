class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max , min = 0,None
        for i in nums:
            max = max+1
            min = 1
        setFun = {i for i in range(min,max+1)}
        setPop = set(nums)
        return list(setFun - setPop)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna