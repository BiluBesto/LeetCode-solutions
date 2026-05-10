class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = 0
        for i in nums: 
            xor = xor^i
        return xor == 0 or len(nums)%2==0