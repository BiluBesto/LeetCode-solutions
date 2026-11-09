class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        seen = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j==i: 
                    continue
                for k in range(n):
                    if k==i or k==j or digits[k]%2!=0:
                        continue
                    newnum = digits[i]*100+digits[j]*10+digits[k]
                    seen.add(newnum)
        return len(seen)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna