class UndergroundSystem:

    def __init__(self):
        self.check_ins = dict()
        self.trips = defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s_out, t_out = stationName, t
        s_in, t_in = self.check_ins[id]

        self.trips[(s_in, s_out)] = tuple(map(add, self.trips[(s_in, s_out)], (t_out - t_in, 1)))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return truediv(*self.trips[(startStation, endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
