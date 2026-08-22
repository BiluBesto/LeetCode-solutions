class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:
            return -1
        return max(len(a),len(b))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna