class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        i=3
        prod=1
        while(n>4):
            if n-i>=0:
                prod*=i
                n-=i
                i=3     
            else:
                i-=1
        prod*=n
        return prod  


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna