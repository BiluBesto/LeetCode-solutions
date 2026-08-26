class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int , date.split('-'))
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if y%400 == 0 or (y%4==0 and y%100!=0):
            days[1] = 29
        return d + sum(days[:m-1])
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna