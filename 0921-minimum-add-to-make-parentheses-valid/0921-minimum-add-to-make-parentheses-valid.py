class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk=[]
        for i in s:
            if i == '(':
                stk.append(i)
            else:
                if len(stk)>0 and stk[-1] == '(':
                    stk.pop()
                else:
                    stk.append(')')
        return len(stk)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna