class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxa = gain[0]
        cur = 0
        for i in gain:
            cur+=i
            maxa = max(cur,maxa)
        return maxa if maxa>0 else 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna