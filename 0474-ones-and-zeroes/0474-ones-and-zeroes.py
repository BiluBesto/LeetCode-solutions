class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0,0):0}
        for s in strs:
            ones = 0
            zeroes = 0
            newdp = {}
            for c in s:
                if c == '1':
                    ones+=1
                else:
                    zeroes+=1
            for key,value in dp.items():
                prevzeroes,prevones=key
                newones,newzeroes = prevones+ones,prevzeroes+zeroes
                if newones<=n and newzeroes<=m:
                    if (newzeroes,newones) not in dp or dp[(newzeroes,newones)]<value+1:
                        newdp[(newzeroes,newones)]=value+1 
            dp.update(newdp)
        return max(dp.values())


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna