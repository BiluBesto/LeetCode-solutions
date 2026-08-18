class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.findNsum(nums,target,4,[],res)
        return res
    
    def findNsum(self,nums,target,N,result,res):
        if len(nums)<N or N<2: 
            return
        if N == 2:
            l,r = 0, len(nums)-1
            while l<r:
                if nums[l]+nums[r]==target:
                    res.append(result + [nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1
        else:
            for i in range(0,len(nums)-N+1):
                if target<nums[i]*N or target>nums[-1]*N:
                    break
                if i == 0 or i> 0 and nums[i-1] != nums[i]:
                    self.findNsum(nums[i+1:],target-nums[i],N-1,result+[nums[i]],res)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna