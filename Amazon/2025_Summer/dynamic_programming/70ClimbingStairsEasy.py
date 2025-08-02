class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2: return n

        mp = [0] * (n + 1)

        mp[1] = 1
        mp[2] = 2

        for r in range(3, n + 1):
            mp[r] = mp[r - 1] + mp[r - 2]

        return mp[n]
