class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = "-" if num<0 else ""
        num = abs(num)
        ans = ""
        while num:
            ans = str(num%7) + ans
            num=num//7
        return sign+ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna