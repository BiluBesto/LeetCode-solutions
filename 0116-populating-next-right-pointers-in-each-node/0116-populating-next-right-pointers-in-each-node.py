"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        root.next = None
        q = deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            p = deque()
            while q:
                p.append(q.popleft())
            l,m,n = None,None,None
            while p:
                l = p.popleft()
                if l is None:
                    while q:
                        x=q.popleft()
                    break
                m = p.popleft()
                q.append(l.left)
                q.append(l.right)
                q.append(m.left)
                q.append(m.right)
                if n is not None:
                    n.next = l
                l.next = m
                n = m
           
        return root


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna