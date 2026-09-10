class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i):
            if i == len(nums):
                res.append(nums.copy())
                return
            for j in range(i,len(nums)):
                nums[j],nums[i] = nums[i],nums[j]
                dfs(i+1)
                nums[j],nums[i] = nums[i],nums[j]
        dfs(0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna