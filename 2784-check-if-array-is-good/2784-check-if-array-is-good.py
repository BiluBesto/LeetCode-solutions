class Solution:
    def isGood(self, nums: List[int]) -> bool:
        x = max(nums)
        if len(nums)>x+1:
            return False
        base = [i for i in range(1,x+1)]
        base.append(x)
        for i in nums:
            if i in base:
                base.remove(i)
        return True if base==[] else False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna