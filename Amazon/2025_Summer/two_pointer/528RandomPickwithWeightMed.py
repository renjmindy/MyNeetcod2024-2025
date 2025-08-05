class Solution:

    def __init__(self, w: List[int]):
        pre = 0
        self.mp = list()

        for r in range(len(w)):
            pre += w[r]
            self.mp.append(pre)

        self.pre = pre

    def pickIndex(self) -> int:
        r = random.randint(1, self.pre)
        return bisect.bisect_left(self.mp, r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
