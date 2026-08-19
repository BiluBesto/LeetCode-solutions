class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        i=0
        while i<len(nums):
            start = nums[i]
            j = i

            while j+1<len(nums) and nums[j+1]==nums[j]+1:
                j+=1
            if nums[j]==start:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[j]}")
            
            i=j+1
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna