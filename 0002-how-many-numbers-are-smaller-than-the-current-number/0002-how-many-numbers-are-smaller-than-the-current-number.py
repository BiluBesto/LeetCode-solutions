class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)):
            ct = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i]>nums[j]:
                    ct+=1
            res.append(ct)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna