class Solution:
    def divisorGame(self, n: int) -> bool:
        res = False
        while(n!=1):
            for i in range(1,n//2+1):
                if n%i == 0:
                    res=not(res)
                    n=n-1
                    break
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna