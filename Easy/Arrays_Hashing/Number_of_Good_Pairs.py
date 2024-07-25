class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        cp = Counter(nums)
        ans = 0

        for k, v in cp.items():
            ans += (v * (v - 1)) // 2

        return ans
