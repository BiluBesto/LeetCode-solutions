class Solution:
    def findComplement(self, num: int) -> int:
        bitlen = num.bit_length()
        mask = (1<<bitlen) - 1
        return num ^ mask

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna