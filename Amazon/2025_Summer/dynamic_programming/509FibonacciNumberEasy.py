class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n

        mp = [0] * (n + 1)
        mp[0] = 0
        mp[1] = 1

        for r in range(2, n + 1):
            mp[r] = mp[r - 1] + mp[r - 2]

        return mp[n]
