class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = nums[::-1]
        ans = [-1] * len(nums)

        for r in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[r]: stack.pop()
            if stack: ans[r] = stack[-1]
            stack.append(nums[r])

        return ans
