class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def solve(amt):
            if amt<0:
                return -1
            if amt==0:
                return 0
            if amt in memo:
                return memo[amt]
            min_count = float('inf')
            for coin in coins:
                res = solve(amt-coin)
                if res!=-1:
                    min_count = min(min_count,1+res)
                
            memo[amt]=min_count if min_count!=float('inf') else -1
            return memo[amt]
        return solve(amount)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna