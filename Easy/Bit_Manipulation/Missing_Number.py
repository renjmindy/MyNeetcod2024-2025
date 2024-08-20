class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans = len(nums)

        for i, num in enumerate(nums):
            #print(i ^ num)
            ans ^= (i ^ num)
            #print(ans)

        return ans
