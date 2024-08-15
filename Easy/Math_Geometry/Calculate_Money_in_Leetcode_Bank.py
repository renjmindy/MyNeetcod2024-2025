class Solution:
    def totalMoney(self, n: int) -> int:

        ans = 0

        for i in range(1, n + 1):
            if i % 7 == 0:
                ans += ((i // 7) - 1) + 7
            else:
                ans += (i // 7) + (i % 7)
        
        return ans
