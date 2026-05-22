# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        
        while cur:
            i = 0
            pre = cur
            while i<k and cur:
                i+=1 
                cur = cur.next
                stack.append(cur)
                
            lat = None
            if cur:
                lat = cur.next
            else:
                break
        
            pre.next = stack.pop()
            cur = pre.next
            while stack:
                cur.next = stack.pop()
                cur = cur.next
            cur.next = lat
    
        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna