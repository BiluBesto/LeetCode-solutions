class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in nums:
            heapq.heappush(minheap,i)
            if len(minheap)>k:
                heapq.heappop(minheap)
        return minheap[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna