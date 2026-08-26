class Solution:
    def balancedStringSplit(self, s: str) -> int:
        m=c=0
        for si in s:
            if si == 'L':
                c+=1
            if si == 'R':
                c-=1
            if c==0: m+=1
        return m

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna