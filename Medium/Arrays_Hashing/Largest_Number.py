from functools import cmp_to_key
class Solution:
    def help(self, a, b):

        if a + b > b + a: return -1
        elif a + b < b + a: return 1
        else: return 0
    
    def largestNumber(self, nums: List[int]) -> str:
        
        ans = list(str(num) for num in nums)
        ans.sort(key=cmp_to_key(self.help))
        
        return ''.join(ans) if ans[0] != '0' else '0'
