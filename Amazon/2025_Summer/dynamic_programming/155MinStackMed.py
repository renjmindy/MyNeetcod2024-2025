class MinStack:

    def __init__(self):
        self.mp = list()

    def push(self, val: int) -> None:
        self.mp.append(val)

    def pop(self) -> None:
        if len(self.mp): self.mp.pop()

    def top(self) -> int:
        if len(self.mp): return self.mp[-1]

    def getMin(self) -> int:
        if len(self.mp): return min(self.mp)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
