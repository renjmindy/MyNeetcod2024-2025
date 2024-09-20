class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        cp = Counter(nums)
        ans = list()

        for k, v in cp.items():
            if v > 1: ans.append(k)

        return ans
