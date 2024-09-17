class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        cp = Counter(nums)
        ans = 0
        
        for k, v in cp.items():
            if v == 1: return -1
            ans += v // 3
            if v % 3 == 2 or v % 3 == 1: ans += 1

        return ans

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        cp = Counter(nums)
        ans = 0
        
        for k, v in cp.items():
            if v == 1: return -1
            ans += ceil(v / 3)

        return ans
