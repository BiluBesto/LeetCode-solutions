# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        res = []

        queue = deque([(root,None,0)])

        while queue:
            if len(res)==2:
                break
            node,parent,depth = queue.popleft()

            if node.val == x or node.val == y:
                res.append((parent,depth))
            if node.left:
                queue.append((node.left,node,depth+1))
            if node.right:
                queue.append(((node.right,node,depth+1)))
        nodex,nodey = res

        return nodex[0]!=nodey[0] and nodex[1] == nodey[1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna