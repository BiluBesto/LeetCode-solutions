class Solution:
    def maxLength(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                X = arr[i:j]
                if math.prod(arr[i:j]) == math.gcd(*X)*math.lcm(*X):
                    print(j-i,i,j,math.gcd(*X),math.lcm(*X))
                    res=max(res,j-i)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna