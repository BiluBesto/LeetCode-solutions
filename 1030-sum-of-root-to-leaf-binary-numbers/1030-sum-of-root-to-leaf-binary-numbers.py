# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, n=0):
            if not node:
                return
            n = 2*n +node.val
            if not node.left and not node.right:
                self.ans+=n
                return
            dfs(node.left,n)
            dfs(node.right,n)
            return
        self.ans = 0
        dfs(root)
        return self.ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna