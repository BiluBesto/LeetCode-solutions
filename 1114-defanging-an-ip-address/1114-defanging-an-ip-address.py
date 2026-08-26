class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in address:
            if i == '.':
                res+="[.]"
                continue
            res+=i
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna