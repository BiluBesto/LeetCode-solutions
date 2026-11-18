class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(0,len(s),2):
            if s[i]!=s[i+1]:
                res+=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna