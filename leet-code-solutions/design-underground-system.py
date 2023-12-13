class UndergroundSystem:

    def __init__(self):
        
        self.station = {}
        self.totalJ = defaultdict(lambda :[0,0])


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.station[id] = (t,stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        t_start,start = self.station[id]
        self.totalJ[(start,stationName)][0] += t-t_start
        self.totalJ[(start,stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        total,totalP = self.totalJ[(startStation,endStation)]
        return total/totalP

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)