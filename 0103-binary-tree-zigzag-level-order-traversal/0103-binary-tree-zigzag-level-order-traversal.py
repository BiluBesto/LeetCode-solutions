# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = [[root.val]]
        ct = 1
        q = deque()
        q.append(root)

        while q:
            cur = []
            p = deque()

            while q:
                p.append(q.popleft())

            while p:
                node = p.popleft()

                if node.left is not None:
                    cur.append(node.left.val)
                    q.append(node.left)

                if node.right is not None:
                    cur.append(node.right.val)
                    q.append(node.right)

            if ct % 2 == 1:
                cur.reverse()

            if cur:
                res.append(cur)

            ct += 1

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna