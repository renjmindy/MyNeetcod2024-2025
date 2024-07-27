class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        cp = Counter(nums)
        ans = 0

        for r in range(max(nums), 0, -1):
            if r in cp: ans += cp[r]
            if ans == r: return ans

        return -1
