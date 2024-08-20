class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        ans = list()

        for i, j in zip(nums[:n], nums[n:]):
            ans.extend((i, j))

        return ans
