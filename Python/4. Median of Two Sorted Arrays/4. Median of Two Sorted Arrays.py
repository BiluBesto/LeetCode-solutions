class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        l=0
        r=len(nums1)-1
        total=len(nums1)+len(nums2)
        half=total//2
        while True:
            i=(l+r)//2 #nums1
            j=half-i-2 #nums2
            n1l=nums1[i] if i>=0 else float("-infinity")
            n1r=nums1[i+1] if i+1 < len(nums1) else float("infinity")
            n2l=nums2[j] if j>=0 else float("-infinity")
            n2r=nums2[j+1] if j+1 < len(nums2) else float("infinity")
            if n1l <= n2r and n2l <= n1r:
                if total%2:
                    return min(n1r,n2r)
                return (max(n1l,n2l) + min(n1r,n2r))/2
            elif n1l > n2r:
                r=i-1
            else:
                l=i+1