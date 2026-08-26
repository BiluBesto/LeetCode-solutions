# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        if self.pred is not None:
            self.ans = min(self.ans,root.val - self.pred)
        self.pred = root.val
        self.inorder(root.right)
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.pred = None
        self.inorder(root)

        return self.ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna