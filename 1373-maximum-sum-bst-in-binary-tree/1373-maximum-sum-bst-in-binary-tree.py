# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.resSum = 0
        def validator(root):
            if not root:
                return 0, float('inf'), float('-inf'), True
            lsum, lmin, lmax, lbst = validator(root.left)
            rsum, rmin, rmax, rbst = validator(root.right)

            if lbst and rbst and lmax < root.val < rmin:
                currentSum = lsum + rsum + root.val
                self.resSum = max(self.resSum, currentSum)
                return currentSum, min(lmin,root.val), max(rmax,root.val), True
            
            return 0, float('-inf'), float('inf'), False

        validator(root)
        return self.resSum