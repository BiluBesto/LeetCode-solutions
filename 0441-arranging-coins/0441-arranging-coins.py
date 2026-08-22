class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left<=right:
            mid = left + (right-left)//2
            coins = mid*(mid+1)//2
            if coins == n:
                return mid
            elif coins<n:
                left = mid+1
            else:
                right = mid - 1

        return right

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna