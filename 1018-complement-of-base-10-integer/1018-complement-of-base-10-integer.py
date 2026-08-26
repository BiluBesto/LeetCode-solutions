class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = n|1
        for i in range(0,5):
            mask |= mask>>(1<<i)
        return n^mask

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna