class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        m = len(word)
        n = len(sequence)
        dp = [0]*(n+1)
        for i in range(n-m,-1,-1):
            if sequence[i:i+m]==word:
                dp[i]=1+dp[i+m]
        print(dp)
        return max(dp)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna