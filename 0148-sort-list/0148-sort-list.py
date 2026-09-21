# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        def findmid(head):
            if head is None or head.next is None:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def merge(head1,head2):
            mergeLL = ListNode(-1)
            temp = mergeLL
            while head1 and head2:
                if head1.val<=head2.val:
                    temp.next = head1
                    head1=head1.next
                else:
                    temp.next = head2
                    head2 = head2.next
                temp = temp.next
            while head1:
                temp.next = head1
                head1 = head1.next
                temp = temp.next
            while head2:
                temp.next = head2
                head2 = head2.next
                temp = temp.next
            return mergeLL.next
        if head is None or head.next is None:
            return head
        mid = findmid(head)
        righthead = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(righthead)
        return merge(left,right)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna