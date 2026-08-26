class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0]*m
        col = [0]*n
        for r,c in indices:
            row[r] ^=1
            col[c] ^=1
        
        oddRows = sum(row)
        oddCols = sum(col)
        
        return oddRows * (n-oddCols) + (m-oddRows) * oddCols

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna