class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []    
        def helper(s,open,close):
            if len(s) == n*2:
                res.append(s)
                return
            if open<n:
                helper(s+'(',open+1, close)
            if close<open:
                helper(s+')',open,close+1)
        helper("",0,0)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna