class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        ans = n // 2

        while n > 1:
            #print(n)
            if n % 2: n = n // 2 + 1
            else: n = n // 2
            ans += n // 2

        return ans
