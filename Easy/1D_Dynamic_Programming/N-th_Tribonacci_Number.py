class Solution:
    def tribonacci(self, n: int) -> int:

        if n <= 1: return n
        if n == 2: return 1
        
        ans = [0] * (n + 1)

        ans[0] = 0
        ans[1] = 1
        ans[2] = 1

        for r in range(3, n + 1):
            ans[r] = sum(ans[r - 3:r])

        return ans[n]
