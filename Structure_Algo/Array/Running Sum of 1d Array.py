class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = list()
        ans.append(nums[0])
        
        for r in range(1, len(nums)):
            ans.append(sum(nums[:r + 1]))
            
        return ans
