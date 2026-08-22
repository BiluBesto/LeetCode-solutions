class NumArray:

    def __init__(self, nums: List[int]):
        self.cache = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            self.cache[i+1] += self.cache[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.cache[right+1] - self.cache[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna