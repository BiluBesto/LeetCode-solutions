class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ch = list(s)
        n = len(ch)
        start = 0
        while start<n:
            end = min(start+k-1,n-1)
            l,r = start,end
            while l<r:
                ch[l],ch[r]=ch[r],ch[l]
                l+=1
                r-=1
            start+=2*k
        return "".join(ch)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna