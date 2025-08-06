class MyCalendarTwo:

    def __init__(self):
        self.mp = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.mp[startTime] = self.mp.setdefault(startTime, 0) + 1
        self.mp[endTime] = self.mp.setdefault(endTime, 0) - 1

        cnts = 0

        for time in self.mp:
            cnts += self.mp[time]
            if cnts > 2:
                # reverse the above operations
                self.mp[startTime] -= 1
                self.mp[endTime] += 1
                return False

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
