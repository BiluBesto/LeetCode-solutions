class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evenCount = 0
        oddCount = 0
        for pos in position:
            if pos % 2:
                oddCount +=1
            else:
                evenCount +=1

        return min(oddCount,evenCount)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna