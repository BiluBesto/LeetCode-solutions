class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)//2
        ct = 0
        res = []
        k = 0
        for i in range(n*2):
            if ct%2==0:
                res.append(nums[k])
            else:
                res.append(nums[k+n])
                k+=1
            ct+=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna