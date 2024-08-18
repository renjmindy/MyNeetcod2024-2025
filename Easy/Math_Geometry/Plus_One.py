class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        new_digits = ''.join([str(digit) for digit in digits])
        new_digits = int(new_digits) + 1
        ans = list()

        while new_digits > 0:
            ans.append(new_digits % 10)
            new_digits //= 10

        return ans[::-1]
