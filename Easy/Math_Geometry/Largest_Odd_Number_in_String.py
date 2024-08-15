class Solution:
    def largestOddNumber(self, num: str) -> str:

        n = len(num)

        while n > 0:
            if int(num[n - 1]) % 2: return num[:n]
            else: n -= 1

        return num[:n]
