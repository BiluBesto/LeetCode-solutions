import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        v = int(''.join(map(str,num)))
        v = v+k
        return [int(i) for i in str(v)]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna