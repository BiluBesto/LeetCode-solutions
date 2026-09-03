# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #root
        #level order traversal "left to right" level by level
        if root is None:
            return []
        q = deque()
        q.append(root)
        result = [[root.val]]
        def bfs(root,p):
            cur = []
            while p:
                q = deque()
                while p:
                    q.append(p.popleft())
                while q:
                    n = q.popleft()
                    if n.left is not None:
                        p.append(n.left)
                        cur.append(n.left.val)
                    if n.right is not None:
                        p.append(n.right)
                        cur.append(n.right.val)
                if cur:
                    result.append(cur)
                cur = []

        bfs(root,q)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna