class Solution:
    def maximum69Number (self, num: int) -> int:
        modif = [int(d) for d in str(num)]
        print(modif)
        for i in range(len(modif)):
            if modif[i]==6:
                modif[i]=9
                break
        return int(''.join(map(str,modif)))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna