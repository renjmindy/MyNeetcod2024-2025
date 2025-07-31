class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0

        mums = list(set(nums))
        mums.sort()
        l, ans = 0, 1 # ans = 1 b/c the length of the starting letter is one

        for r in range(1, len(mums)):
            if mums[r] - mums[r - 1] == 1: 
                ans = max(ans, r - l + 1) # update consecutive sequence length
            else: 
                l = r # reset

        return ans
