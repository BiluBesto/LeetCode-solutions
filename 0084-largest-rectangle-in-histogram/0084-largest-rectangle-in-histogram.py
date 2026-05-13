class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1]*n, [n]*n
        stack = []
        resMax = 0
        for i in range(n):
            while stack and heights[i]<= heights[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack.clear()

        for i in range(n-1,-1,-1):
            while stack and heights[i]<= heights[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        stack.clear()

        for i in range(n):
            width = right[i] - left[i] - 1
            resMax = max(resMax, heights[i]*width)
        
        return resMax

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna