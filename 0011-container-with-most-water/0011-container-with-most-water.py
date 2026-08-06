class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height) - 1
        while l<r:
            area = (r-l)*min(height[l],height[r])
            res = max(res,area)

            if height[l]>=height[r]:
                r-=1
            else:
                l+=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna