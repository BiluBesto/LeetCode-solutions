class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        total = 0
        for ch in s:
            w = widths[ord(ch)-ord('a')]
            if total+w>100:
                lines+=1
                total = 0
            total+=w

        return [lines,total]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna