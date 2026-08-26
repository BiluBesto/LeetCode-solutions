class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mpp = [0]*100
        count = 0
        for a,b in dominoes:
            key = a*10 +b if a<=b else b*10+a
            count += mpp[key]
            mpp[key]+=1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna