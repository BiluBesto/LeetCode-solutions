class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum=0
        for x in range(max(1,n-k),n+k+1):
             if n&x==0:
                sum+=x
        return sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna