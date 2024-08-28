class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        ans = [1] * len(nums)
        for r in range(len(nums)):
            ans[r] *= prod
            prod *= nums[r]

        prod = 1
        for r in range(len(nums) - 1, -1, -1):
            ans[r] *= prod
            prod *= nums[r]

        return ans
