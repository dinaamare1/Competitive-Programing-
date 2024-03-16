class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = ListNode(homepage)      
    def visit(self, url: str) -> None:
        curr = ListNode(url)
        curr.prev = self.history
        self.history.next = curr
        self.history = curr
    def back(self, steps: int) -> str:
        # name = self.history
        # for i in range(steps):
        #     if name.prev:
        #         name = name.prev
        #     else:
        #         break
        # self.history = name
        # return name.val if name else None
        while self.history.prev and steps>0:
            self.history = self.history.prev
            steps -= 1
        return self.history.val

    def forward(self, steps: int) -> str:
        # name = self.history
        # for i in range(steps):
        #     if name.next:
        #         name = name.next
        #     else:
        #         break
        # self.history = name
        # return name.val if name else None
        while self.history.next and steps>0:
            self.history = self.history.next
            steps -= 1
        return self.history.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)