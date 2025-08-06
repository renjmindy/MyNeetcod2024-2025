class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x <= 1: return x

        l, r = 1, x // 2

        while l <= r:
            pivot = l + (r - l) // 2
            if pivot ** 2 == x: return pivot
            elif pivot ** 2 < x: l = pivot + 1
            else: r = pivot - 1

        return r
