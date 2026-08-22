class Solution:
    def reverseWords(self, s: str) -> str:
        start,end=0,0
        sc = list(s)
        for i in range(len(s)):
            if s[i]==' ':
                end = i-1
                while start<end:
                    sc[start],sc[end]=sc[end],sc[start]
                    start+=1
                    end-=1
                start=i+1
        end = len(s)-1
        while start<end:
            sc[start],sc[end]=sc[end],sc[start]
            start+=1
            end-=1
        return ''.join(sc)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna