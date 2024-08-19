class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        mums = Counter(nums)

        for k, v in mums.items():
            if v == 1: return k

        return -1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0

        for num in nums:
            ans ^= num

        return ans
