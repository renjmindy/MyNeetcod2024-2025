class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        l, r = 0, 0

        while r < len(nums):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        return nums
