class OrderedStream:

    def __init__(self, n: int):
        self.cont = [""]*(n+1)
        self.ptr = 1  
        self.n = n    
    def insert(self, idKey: int, value: str) -> List[str]:
        chunk = []
        self.cont[idKey] = value
        while self.ptr<= self.n and self.cont[self.ptr] != "":
            chunk.append(self.cont[self.ptr])
            self.ptr+=1
        return chunk


        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)