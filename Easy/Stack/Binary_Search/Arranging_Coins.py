class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        l, r = 1, n + 1

        while l <= r:
            pivot = l + (r - l) // 2
            coins = (pivot * (pivot + 1)) // 2
            if coins == n: return pivot
            elif coins < n: l = pivot + 1
            else: r = pivot - 1

        return r
