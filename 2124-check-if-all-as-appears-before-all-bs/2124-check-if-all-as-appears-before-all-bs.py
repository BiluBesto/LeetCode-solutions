class Solution:
    def checkString(self, s: str) -> bool:
        fenc = False
        for i in s:
            if i == 'b':
                fenc = True
            elif fenc == True:
                return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna