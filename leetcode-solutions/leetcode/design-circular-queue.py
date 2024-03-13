class MyCircularQueue:

    def __init__(self, k: int):
        self.queue =[]
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if len(self.queue) != self.size:
            self.queue.append(value)
            # print(self.queue,self.size,len(self.queue))
            return True
        return False       

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            return True 
        return False       
    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
        return -1 
        
    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
        return -1
    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        return False
    def isFull(self) -> bool:
        if len(self.queue) != self.size:
            return False
        return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()