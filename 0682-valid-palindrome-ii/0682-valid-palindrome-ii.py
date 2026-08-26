class Solution:
    def validPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s)-1
        while p1<=p2:
            if s[p1]!=s[p2]:
                s1 = s[:p1]+s[p1+1:]
                s2 = s[:p2]+s[p2+1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
            p1+=1
            p2-=1
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna