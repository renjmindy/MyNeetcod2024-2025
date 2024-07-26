class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        duplicated = sum(nums) - sum(set(nums))
        missing = (len(nums) * (len(nums) + 1)) // 2 - sum(set(nums))

        return [duplicated, missing] 

