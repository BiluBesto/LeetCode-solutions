class Solution:
    def findCombinations(self,index,target,candidates,current,result):
        if target==0:
            result.append(current[:])
            return
        
        for i in range(index, len(candidates)):
            if candidates[i]<=target:
                current.append(candidates[i])
                self.findCombinations(i,target-candidates[i],candidates,current,result)
                current.pop()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.findCombinations(0,target,candidates,[],result)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna