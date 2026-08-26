class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        n = len(s)
        i = 0
        while i <n and s[i]!=c:
            i+=1
        idx = 0
        for idx in range(i+1):
            ans.append(abs(idx-i))
        ans.pop()
        j = 0
        while j<n:
            while i<n and s[i]!=c:
                i+=1
            j = i + 1
            while j<n and s[j]!=c:
                j+=1
            while idx<n and idx<=j:
                if j<n:
                    ans.append(min(abs(idx-i),abs(idx-j)))
                else:
                    ans.append(abs(idx-i))
                idx+=1
            i=j
        return ans            

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna