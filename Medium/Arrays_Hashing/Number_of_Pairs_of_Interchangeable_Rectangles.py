class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        mp = defaultdict(int)

        for rec in rectangles:
            mp[rec[0] / rec[1]] += 1

        return sum([(v * (v - 1)) // 2 for k, v in mp.items() if v > 1])
