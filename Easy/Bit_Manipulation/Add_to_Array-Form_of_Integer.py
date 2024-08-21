import sys
sys.set_int_max_str_digits(10**6)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        num = int(''.join([str(c) for c in num])) + k

        return [int(c) for c in str(num)]

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        carry = 0
        ans = list()

        for r in range(len(num) - 1, -1, -1):
            total = carry + num[r] + k % 10
            carry = total // 10
            ans.append(total % 10)
            k //= 10

        while k:
            total = carry + k % 10
            carry = total // 10
            ans.append(total % 10)
            k //= 10    

        if carry: ans.append(carry)

        return ans[::-1]
