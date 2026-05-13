# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root,result):
        if not root:
            return
        
        self.postorder(root.left,result)
        self.postorder(root.right,result)
        result.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorder(root,result)
        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna