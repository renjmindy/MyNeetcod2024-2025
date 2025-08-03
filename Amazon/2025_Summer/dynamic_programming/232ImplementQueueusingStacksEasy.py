class MyQueue:

    def __init__(self):
        self.mp = list()

    def push(self, x: int) -> None:
        self.mp.append(x)

    def pop(self) -> int:
        return self.mp.pop(0)

    def peek(self) -> int:
        if len(self.mp): return self.mp[0]

    def empty(self) -> bool:
        return len(self.mp) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
