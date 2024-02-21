# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = list1
        left = dummy
        right = list2
        while left and left.next and right:
            if left.next.val >= right.val:
                temp = right.next
                right.next = left.next
                left.next = right
                right = temp
            left = left.next
        if not left.next:
            left.next = right
        return dummy.next


                

        