# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        odd = dummy.next
        if odd and odd.next:
            even = dummy.next.next
            even_start = even
            while even and even.next:
                odd.next = odd.next.next
                even.next = even.next.next
                even = even.next
                odd = odd.next
            odd.next = even_start
        return dummy.next