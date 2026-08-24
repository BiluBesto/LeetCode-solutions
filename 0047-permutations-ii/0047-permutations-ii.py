class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited=[False]*len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                    continue
                visited[i]=True
                curr.append(nums[i])

                dfs(curr)

                curr.pop()
                visited[i] = False
        dfs([])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna