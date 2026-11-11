class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        pairs = min(need1,need2)
        cost_pairs = pairs*min(costBoth, cost1+cost2)
        rem1 = need1 - pairs
        rem2 = need2 - pairs
        cost_rem = rem1*min(cost1,costBoth) +rem2*min(cost2,costBoth)
        return cost_pairs + cost_rem

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna