# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        cur,rmin  = 0,float('inf')
        def dfs(root):
            nonlocal cur, rmin
            if not root:
                return
            cur= cur+1
            if not root.left and not root.right:
                rmin = min(rmin,cur)
            dfs(root.left)
            dfs(root.right)
            cur-=1
        dfs(root)

        return rmin if root else 0