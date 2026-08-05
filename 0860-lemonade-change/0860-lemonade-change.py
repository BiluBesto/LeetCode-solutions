class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ct5 = 0
        ct10 = 0
        for i in bills:
            if i == 5:
                ct5+=1
            elif i==10 and ct5>=1:
                ct10+=1
                ct5-=1
            elif i==20:
                if ct10>=1 and ct5>=1:
                    ct10-=1
                    ct5-=1
                elif ct5>=3:
                    ct5-=3
                else:
                    return False
            else:
                return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna