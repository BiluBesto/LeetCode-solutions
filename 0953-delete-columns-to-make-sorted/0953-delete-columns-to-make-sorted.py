class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if strs[row][col] < strs[row-1][col]:
                    res+=1
                    break
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna