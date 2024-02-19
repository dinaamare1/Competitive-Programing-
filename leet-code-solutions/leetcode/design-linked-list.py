class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = ListNode() # this is the same as getting a dummy node
        self.n = 0 # this is to keep track of the length of the linked List

    def get(self, index):
        if index + 1 <0 or index + 1 > self.n:
            return -1
        curr = self.head  # starts from the dummy node
        idx = 0
        # while curr:
        #     if idx == index + 1: # since it started with the dummy node I added + 1
        #         return curr.val
        #     curr = curr.next
        #     idx += 1
        # return -1

        # while index + 1 > 0:
        #     curr = curr.next 
        #     index -= 1
        # return curr.val
        for _ in range(index+1):
            if curr:
                curr = curr.next
        return curr.val if curr else -1
        

    def addAtHead(self, val):
        # Add a node of value val before the first element of the linked list
        # new_node = ListNode(val)
        # new_node.next = self.head.next
        # self.head.next = new_node
        self.addAtIndex(0,val)
        # self.n += 1

    def addAtTail(self, val):
        # Append a node of value val as the last element of the linked list
        # current = self.head
        # while current.next:
        #     current = current.next
        # current.next = ListNode(val)
        self.addAtIndex(self.n,val)
        # self.n += 1

    def addAtIndex(self, index, val):
        # Add a node of value val before the indexth node in the linked list
        if index + 1 < 0 and index > self.n:
            return 
        new_node = ListNode(val)
        curr = self.head
        idx = 0
        while curr and idx < index:
            curr = curr.next
            idx += 1
        if curr:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
    def deleteAtIndex(self, index):
        if index + 1 <0 and index > self.n:
            return
        curr = self.head
        idx = 0
        while curr and idx < index:
            curr = curr.next
            idx += 1
        if index < self.n and curr.next:
            curr.next = curr.next.next
            self.n -= 1
