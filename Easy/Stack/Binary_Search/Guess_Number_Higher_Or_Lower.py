# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l, r = 1, n + 1

        while l <= r:
            pivot = l + (r - l) // 2
            if guess(pivot) == 0: return pivot
            elif guess(pivot) == 1: l = pivot + 1
            else: r = pivot - 1

        
