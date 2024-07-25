class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        pattern = nums[0] < nums[len(nums) - 1]

        return all((nums[i] < nums[i + 1]) == pattern or (nums[i] == nums[i + 1]) for i in range(len(nums) - 1))
