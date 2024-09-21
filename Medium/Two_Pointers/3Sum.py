class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]: continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                pre = nums[i] + nums[l] + nums[r]
                if pre < 0: l += 1
                elif pre > 0: r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    r -= 1

        return ans
