# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        if head is None or head.next is None:
            return head
        arr = [head.val]
        while head.next:
            head=head.next
            arr.append(head.val)
        arr.sort()
        cur = dummy
        for i in arr:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna