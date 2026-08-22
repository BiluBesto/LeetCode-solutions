class Solution:
    def checkRecord(self, s: str) -> bool:
        act = 0
        lct = 0
        for i in range(len(s)):
            if s[i]=='P':
                lct=0
                continue
            elif s[i]=='A':
                act+=1
                if act>=2:
                    return False
                lct = 0
            elif s[i]=='L':
                lct+=1
                if lct>=3:
                    return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna