class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l, r = 0, 0
        ans = list()

        for i in range(len(nums)):
            if i % 2 == 0:
                while r < len(nums) and nums[r] < 0:
                    r += 1
                ans.append(nums[r])
                r += 1
            else:
                while l < len(nums) and nums[l] > 0:
                    l += 1
                ans.append(nums[l])
                l += 1

        return ans
