class Solution:
    def backsend(self,nums,start,end):
        while start<end:
            nums[start],nums[end] = nums[end], nums[start]
            start+=1
            end-=1
    def nextPermutation(self, nums: List[int]) -> None:
        idx = -1
        length = len(nums)
        for i in range(length-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx = i
                break
        if idx==-1:
            self.backsend(nums,0,length-1)
            return

        self.backsend(nums,idx+1,length-1)
        jj=-1
        for j in range(idx+1,length):
            if nums[idx]<nums[j]:
                nums[idx],nums[j] = nums[j], nums[idx]
                break
       


        #no returning

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna