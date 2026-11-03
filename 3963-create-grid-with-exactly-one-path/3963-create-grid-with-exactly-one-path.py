class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        for i in range(m-1):
            cur = "."
            for j in range(1,n):
                cur+="#"
            res.append(cur)
        newcur = "."
        for i in range(n-1):
            newcur+='.'
        res.append(newcur)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna