class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        l, r = 0, len(digits) - 1
        
        while l <= r:
            if digits[r] == 9: digits[r] = 0; r -= 1
            else: digits[r] += 1; return digits
            
        return [1] + digits
