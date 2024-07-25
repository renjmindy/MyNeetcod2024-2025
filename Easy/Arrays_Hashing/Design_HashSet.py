class MyHashSet:

    def __init__(self):
        self.ans = set()

    def add(self, key: int) -> None:
        self.ans.add(key) 

    def remove(self, key: int) -> None:
        if self.contains(key): self.ans.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.ans


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
