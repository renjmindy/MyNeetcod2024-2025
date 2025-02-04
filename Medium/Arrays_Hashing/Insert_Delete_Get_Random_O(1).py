class RandomizedSet:

    def __init__(self):
        self.ans = list()

    def insert(self, val: int) -> bool:
        if val not in self.ans: 
            self.ans.append(val)
            return True
        else: return False

    def remove(self, val: int) -> bool:
        if val in self.ans:
            self.ans.remove(val)
            return True
        else: return False

    def getRandom(self) -> int:
        return choice(self.ans)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
