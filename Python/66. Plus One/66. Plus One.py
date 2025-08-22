class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for ind in range(len(digits) - 1, -1, -1):
            digits[ind] += 1
            if digits[ind] < 10:
                return digits
            digits[ind] = 0
        return [1] + digits