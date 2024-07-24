class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    
        mums = set(nums)
        ans = list()

        for r in range(1, len(nums) + 1):
            if r not in mums: ans.append(r)

        return ans 
