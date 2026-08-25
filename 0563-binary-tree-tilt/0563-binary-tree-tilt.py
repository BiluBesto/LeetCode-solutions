# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def dfs(root):
            if not root:
                return 0
            l,r = 0,0
            nonlocal sum
            l+=dfs(root.left)
            r+=dfs(root.right)
            sum+=abs(l-r)
            return root.val+l+r
        dfs(root)
        return sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna