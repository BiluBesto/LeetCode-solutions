class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        count = 0
        limit = len(candyType)//2
        res = set(candyType)
        for i in res:
            if count<limit:
                count+=1
            else:
                break
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna