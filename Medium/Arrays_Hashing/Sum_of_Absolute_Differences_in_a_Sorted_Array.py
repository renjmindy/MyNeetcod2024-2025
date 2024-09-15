class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        pre, tot = 0, sum(nums)
        ans = list()

        for i in range(len(nums)):
            pre += nums[i]
            x = ((i + 1) * nums[i] - pre) + (tot - pre - (len(nums) - i - 1) * nums[i])
            ans.append(x)

        return ans
