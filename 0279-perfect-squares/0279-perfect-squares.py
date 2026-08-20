class Solution:
    def numSquares(self, n: int) -> int:
        if math.isqrt(n) ** 2 == n:
            return 1
        temp = n
        while temp%4==0:
            temp//=4
        if temp%8==7:
            return 4
        for i in range(1,math.isqrt(n)+1):
            if math.isqrt(n-i*i)**2==n-i*i:
                return 2
        return 3

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna