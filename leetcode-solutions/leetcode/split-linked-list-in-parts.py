# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length ,curr = 0,head
        while curr:
            length += 1
            curr = curr.next
        splited_len,extra_containing = length//k,length % k
        ans = []
        curr = head
        for i in range(k):
            ans.append(curr)
            if extra_containing:
                for i in range(splited_len):
                    if not curr:break
                    curr = curr.next
            else:
                for i in range(splited_len-1):
                    if not curr:break
                    curr = curr.next
            if extra_containing:
                extra_containing -= 1
            if curr:
                curr.next,curr = None,curr.next
        return ans
        