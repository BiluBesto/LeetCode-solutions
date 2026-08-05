class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prevVal = groups[0]
        res = []
        res.append(words[0])
        for i in range(1,len(words)):
            if groups[i]!=prevVal:
                prevVal = 0 if prevVal==1 else 1
                res.append(words[i])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna