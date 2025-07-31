class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        sign = 1 if x > 0 else -1

        if sign == -1 and x * sign > 0: return False

        x *= sign

        y = [c for c in str(x)][::-1]

        return list(str(x)) == y
