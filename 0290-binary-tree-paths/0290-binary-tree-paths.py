# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node,path, result):
            if not node:
                return
            path+=str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                dfs(node.left,path + "->",result)
                dfs(node.right,path + "->",result)
        result = []
        dfs(root,"",result)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna