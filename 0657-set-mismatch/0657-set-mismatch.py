class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        mp ={i:1 for i in range(1,n+1)}

        for a in nums:
            mp[a]-=1

        duplicate,missing = 0,0

        for key,value  in mp.items():
            if value == -1:
                duplicate = key
            if value ==1:
                missing = key
        return [duplicate,missing]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna