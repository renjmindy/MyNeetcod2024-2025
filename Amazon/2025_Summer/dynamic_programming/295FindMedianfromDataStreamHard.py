class MedianFinder:

    def __init__(self):
        self.mp = list()

    def addNum(self, num: int) -> None:
        self.mp.append(num)

    def findMedian(self) -> float:
        self.mp.sort()
        if len(self.mp) % 2:
            return self.mp[len(self.mp) // 2]
        else:
            return (self.mp[len(self.mp) // 2 - 1] + self.mp[len(self.mp) // 2]) / 2
