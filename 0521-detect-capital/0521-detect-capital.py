class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True

        if 'A' <= word[0] <= 'Z':
            flagc = 'A' <= word[1] <= 'Z'
        else:
            flagc = False
        for i in range(1,len(word)):
            if flagc:
                if 'a'<=word[i]<='z':
                    return False
            else:
                if 'A'<=word[i]<='Z':
                    return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna