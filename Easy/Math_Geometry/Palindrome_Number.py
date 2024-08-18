class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False

        y = list()

        while x > 0:
            y.append(x % 10)
            x //= 10

        ans = ''.join(str(num) for num in y)

        return ans == ans[::-1]
