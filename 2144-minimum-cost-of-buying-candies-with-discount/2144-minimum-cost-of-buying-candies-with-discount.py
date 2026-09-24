class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse = True)
        res = 0
        ct = 0
        for i in cost:
            if ct == 2:
                ct=0
                continue
            res+=i
            ct+=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna