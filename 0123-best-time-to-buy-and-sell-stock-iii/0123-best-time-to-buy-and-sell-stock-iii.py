class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1, s1  = float('-inf'), float('-inf')
        b2, s2 = float('-inf') , float('-inf')

        for p in prices:
            b1 = max(b1,-p)
            s1 = max(s1, b1+p)
            b2 = max(b2, s1-p)
            s2 = max(s2, b2+p)
        return s2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna