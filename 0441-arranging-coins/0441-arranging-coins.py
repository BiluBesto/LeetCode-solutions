class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        c = 0
        while n>0:
            if n-i>=0:
                c+=1
                n = n-i
                i+=1
            else:
                break
        return c

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna