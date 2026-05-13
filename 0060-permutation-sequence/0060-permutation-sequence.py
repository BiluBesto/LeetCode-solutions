class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        res = []
        vals = list(range(1,n+1))
        k-=1
        fact = factorial(n)//n
        while vals:
            res.append(str(vals[k//fact]))
            vals.pop(k//fact)
            if not vals:
                break
            k%=fact
            fact//=len(vals)


        return ''.join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna