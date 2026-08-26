class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year,month,day).strftime('%A')

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna