class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = Counter(nums)
        for key,value in n.items():
            if value == len(nums)//2:
                return key

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna