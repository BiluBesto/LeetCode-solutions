class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSum = 0
        freq = {0:1}
        count = 0
        for i in nums:
            prefSum += i

            if prefSum - k in freq:
                count+=freq[prefSum-k]
            freq[prefSum] = freq.get(prefSum,0)+1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna