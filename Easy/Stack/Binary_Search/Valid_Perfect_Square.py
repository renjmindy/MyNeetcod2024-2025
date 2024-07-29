class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num <= 1: return True

        l, r = 1, num // 2

        while l <= r:
            pivot = l + (r - l) // 2
            if pivot ** 2 == num: return True
            elif pivot ** 2 > num: r = pivot -1
            else: l = pivot + 1

        return False
