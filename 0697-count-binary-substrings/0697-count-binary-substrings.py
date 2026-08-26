class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        prev = 0
        strk = 1

        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                strk+=1
            else:
                prev = strk
                strk = 1
            if strk<=prev:
                res +=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna