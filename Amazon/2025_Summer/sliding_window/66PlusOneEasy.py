class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = int(''.join([str(digit) for digit in digits]))

        n += 1

        return [int(c) for c in str(n)]
