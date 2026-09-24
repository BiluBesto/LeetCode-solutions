class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        res = []
        for x in str(n):
            if x!='0':
                res.append(int(x))
        sm = sum([x for x in res])
        x = int("".join(map(str,res)))
        return x * sm


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna