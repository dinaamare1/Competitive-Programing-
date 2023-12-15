class FrequencyTracker:

    def __init__(self):
        self.dic=defaultdict(int)
        self.freq=defaultdict(int)
    def add(self, number: int) -> None:
        pre=self.dic[number]
        self.dic[number]+=1
        self.freq[self.dic[number]]+=1
        self.freq[pre]-=1
    def deleteOne(self, number: int) -> None:
        if self.dic[number]:
            pre=self.dic[number]
            self.dic[number]-=1
            self.freq[self.dic[number]]+=1
            self.freq[pre]-=1
    def hasFrequency(self, frequency: int) -> bool:
        if self.freq[frequency]> 0:
            return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)