class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct=0
        n=nums[0]
        for j in nums:
            if ct==0:
                n=j
            ct= ct + (1 if n==j else -1)
        return n