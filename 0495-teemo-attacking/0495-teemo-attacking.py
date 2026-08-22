class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries)):
            if i!=len(timeSeries)-1:
                if timeSeries[i+1]-timeSeries[i]>=duration:
                    ans+=duration
                else:
                    ans+=timeSeries[i+1]-timeSeries[i]
            else:
                ans+=duration

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna