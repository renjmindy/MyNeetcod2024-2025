class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.ans = nums
        self.sel = k

    def add(self, val: int) -> int:
        self.ans.append(val)
        self.ans.sort()
        return self.ans[::-1][self.sel - 1]
