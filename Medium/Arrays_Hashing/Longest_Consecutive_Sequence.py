class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mums = list(set(nums))
        mums.sort()
        print(mums)

        l, ans = 0, 0

        for r in range(1, len(mums)):
            if mums[r] - mums[r - 1] != 1:
                ans = max(ans, r - l)
                l = r

        ans = max(ans, len(mums) - l)
        return ans
                

        return 0
