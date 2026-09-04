class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefSum = 0
        prefSumCount = {0:1}

        for num in nums:
            prefSum += num
            if prefSum - k in prefSumCount:
                count+=prefSumCount[prefSum-k]
            if prefSum in prefSumCount:
                prefSumCount[prefSum]+=1
            else:
                prefSumCount[prefSum]=1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna