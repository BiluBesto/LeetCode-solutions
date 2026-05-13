class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        resMax = 0
        heights = [0]*(n+1) # 1 extra 0 is purposefully used

        for row in matrix:
            for c in range(n):
                heights[c] = heights[c] + 1 if row[c]=='1' else 0
            
            stack = [-1]
            for j in range(n+1):
                while stack[-1]!=-1 and heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j-stack[-1]-1
                    resMax = max(resMax,h*w)
                stack.append(j)
        return resMax


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna