class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = [0]*len(seq)
        for i in range(len(seq)):
            if seq[i] == '(':
                depth+=1
                ans[i] = depth%2
            else:
                ans[i] = depth%2
                depth-=1
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna