class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        stack = [s[0]]
        s+="$"

        for i in range(1,len(s)):
            if s[i]!=stack[-1]:
                if len(stack)>=3:
                    ans.append([i-len(stack),i-1])
                stack = []
            stack.append(s[i])
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna