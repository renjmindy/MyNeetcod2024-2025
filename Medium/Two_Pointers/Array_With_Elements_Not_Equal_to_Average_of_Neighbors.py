class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        l, r = 0, len(nums) - 1
        ans = list()

        while l < r:
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r -= 1

        if ans[-1] != nums[l]: ans.append(nums[l])

        return ans

        
