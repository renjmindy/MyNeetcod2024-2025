class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        mp = Counter(nums)

        for k, v in mp.items():
            if v > 1: return k

        return -1
