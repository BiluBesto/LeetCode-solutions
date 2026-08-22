class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False
        mappings = {}
        i = 0 
        print(len(s))
        for c in pattern:
            curStr = ""
            while i<len(s) and s[i]!=" ":
                curStr += s[i]
                i+=1
            i+=1
            if c in mappings:
                if mappings[c]!=curStr:
                    return False
            else:
                if curStr in mappings.values():
                    return False
                mappings[c] = curStr
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna