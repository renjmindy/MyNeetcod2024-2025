class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)
        tot = sum(nums)

        for num in nums:
            if num < tot - num: continue
            else: tot -= num

        return tot if tot > 0 else -1
