class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1 if x > 0 else -1

        x *= sign

        n = int(''.join([c for c in str(x)][::-1]))

        return sign * n if sign * n <= (2**31 - 1) and sign * n >= -2**31 else 0
