class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        np = Counter(nums)
        
        sp = list()
        
        for k, v in np.items():
            if v == 1: sp.append(k)
                
        sp.sort()
        
        return sp[-1] if len(sp) > 0 else -1
