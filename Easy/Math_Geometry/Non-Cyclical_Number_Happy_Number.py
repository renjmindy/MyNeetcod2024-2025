class Solution:
    def help(self, n):

        ans = 0

        while n > 0:
            ans += (n % 10) ** 2
            n //= 10

        return ans

    def isHappy(self, n: int) -> bool:
        
        ans = list()

        while n > 1:
            n = self.help(n)
            if n not in ans: ans.append(n)
            else: return False

        return True
