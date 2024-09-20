class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        ones, zeros, ans = 0, 0, 0
        diff = dict()

        for i, num in enumerate(nums):
            if num == 1: ones += 1
            else: zeros += 1
            if ones - zeros not in diff: 
                diff[ones - zeros] = i
            if ones == zeros: ans = ones + zeros
            else: 
                #print(ones - zeros)
                idx = diff[ones - zeros]
                ans = max(ans, i - idx)

        return ans
