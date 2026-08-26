class Solution:
    def isPrime(self,n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0

        for i in range(left,right+1):
            setBits = bin(i).count('1')
            if self.isPrime(setBits):
                count+=1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna