class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for char in range(ord('a'),ord('z')+1):
            char = chr(char)
            minc = float('inf')

            for word in words:
                count = word.count(char)
                minc = min(minc,count)
                if minc == 0:
                    break
            res.extend([char]*minc)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna