class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        n = len(arr)
        minDiff = 2e6+1
        for i in range(1,n):
            diff = arr[i]-arr[i-1]
            if diff<minDiff:
                minDiff = diff
                res = [[arr[i-1],arr[i]]]
            elif diff == minDiff:
                res.append([arr[i-1],arr[i]])

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna