class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mappings = {}
        for i in knowledge:
                mappings[i[0]] = i[1]
        i=0
        j=0
        res = ""
        skipflag = False
        for idx in range(len(s)):
            if s[idx] == '(' and idx+1<len(s):
                i = idx+1
                skipflag = True
            elif not skipflag:
                res+=s[idx]
            elif s[idx] == ')':
                j = idx-1
                skipflag = False
                if s[i:j+1] in mappings:
                    res+=mappings[s[i:j+1]]
                else:
                    res+='?'
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna