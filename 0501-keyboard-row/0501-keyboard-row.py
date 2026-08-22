class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        m = {}

        for c in "qwertyuiop":
            m[c]=1
        for c in "asdfghjkl":
            m[c]=2
        for c in "zxcvbnm":
            m[c]=3
        ans = []
        for  w in words:
            lw = w.lower()
            r = m[lw[0]]
            if all(m[ch]==r for ch in lw):
                ans.append(w)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna