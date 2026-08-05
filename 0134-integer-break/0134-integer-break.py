class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        threes = n//3
        remainder = n%3
        if remainder==1:
            threes-=1
            remainder = 4
        elif remainder == 0:
            remainder = 1
        return remainder*(3**threes)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna