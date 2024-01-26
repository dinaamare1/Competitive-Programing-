class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        prev = None
        temp = None
        n = 0
        if right-left ==0:
            return dummy.next
        while curr and n < left:
            prev = curr
            curr = curr.next
            n += 1
        while curr and n<=right:
            prev_node = curr.next
            curr.next = temp
            temp = curr
            curr = prev_node
            n+= 1
        if prev: #checks if there is a previous node to stick the reversed temp
            prev.next.next = curr
            prev.next = temp
        else:
            dummy.next = temp
        return dummy.next
