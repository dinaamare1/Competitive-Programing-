# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        start,end = dummy,dummy
        while end and n>0:
            end = end.next
            n-= 1
        while end and end.next:
            start = start.next
            end = end.next
        if start and start.next:
            start.next = start.next.next
        else:
            dummy.next = dummy.next.next
        return dummy.next
        