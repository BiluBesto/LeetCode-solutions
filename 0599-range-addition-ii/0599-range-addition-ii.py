class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        minrow = m
        mincol = n
        for i in range(len(ops)):
            minrow = min(minrow,ops[i][0])
            mincol = min(mincol,ops[i][1])

        return minrow * mincol

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna