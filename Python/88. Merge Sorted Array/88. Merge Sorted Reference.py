class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        for i in nums2:
            nums1.append(i)
        nums1.sort()
