class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Coaching: Your logic for handling duplicates is correct! 
        # You are using the 'include/exclude' pattern and skipping duplicates during the 'exclude' phase.
        #
        # BUG ALERT: You are using 'res' but it is not defined. You must initialize 'res = []' before the helper.
        #
        # Complexity Analysis:
        # Time Complexity: O(n * 2^n) - There are 2^n possible subsets, and copying each subset takes O(n).
        # Space Complexity: O(n) - For the recursion stack and the 'subset' list.
        # This is the optimal complexity for this problem.
        
        res = [] # Added missing initialization
        subset = []
        nums.sort()
        def helper(i):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            helper(i+1)
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            helper(i+1)
        helper(0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna