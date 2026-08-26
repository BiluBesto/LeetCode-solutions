class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        while i +1<n and arr[i]<arr[i+1]:
            i+=1
        if i == 0 or i == n - 1:
            return False
        while i+1<len(arr) and arr[i]>arr[i+1]:
            i+=1
        return i==n-1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna