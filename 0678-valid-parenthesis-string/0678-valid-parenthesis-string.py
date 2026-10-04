class Solution:
    def checkValidString(self, s: str) -> bool:
        low,high = 0,0
        for c in s:
            if c == '(':
                low+=1
                high+=1
            elif c==')':
                low-=1
                high-=1
            else:
                low-=1
                high+=1
            if high<0:
                return False
            if low<0:
                low = 0
        return low==0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna