class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse =True)
        medals = ["Gold Medal","Silver Medal","Bronze Medal"]
        rank_mapping = {score:medals[i] if i<3 else str(i+1) for i, score in enumerate(sorted_score)}
        return [rank_mapping[score] for score in score]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna