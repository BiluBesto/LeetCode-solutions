# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.merge(root1,root2)
    def merge(self,r1,r2):
        if r1 is None:
            return r2
        if r2 is None:
            return r1
        r1.val+=r2.val

        r1.left = self.merge(r1.left,r2.left)
        r1.right = self.merge(r1.right,r2.right)

        return r1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna