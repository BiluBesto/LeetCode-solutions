# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, root, subRoot):
        if subRoot is not None and root is not None:
            if root.val == subRoot.val:
                return self.isSame(root.left,subRoot.left) and self.isSame(root.right,subRoot.right)
            return False
        if subRoot == root:
            return True
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is not None:
            if root.val == subRoot.val:
                if self.isSame(root,subRoot):
                    return True
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna