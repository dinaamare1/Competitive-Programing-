# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sets = set()
        curr1,curr2 = headA,headB
        while curr1:
            sets.add(curr1)
            curr1= curr1.next
        while curr2:
            if curr2 in sets:
                return curr2            
            curr2 = curr2.next
        return None
        