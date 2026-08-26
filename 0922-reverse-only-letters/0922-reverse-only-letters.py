class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start = 0
        end = len(s)-1
        s = list(s)

        while True:
            if start>=end:
                break
            if s[start].isalpha() and s[end].isalpha():
                s[start],s[end] = s[end],s[start]
                start+=1
                end-=1
            elif not s[start].isalpha():
                start+=1
            else:
                end-=1
            
        return ''.join(s)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna