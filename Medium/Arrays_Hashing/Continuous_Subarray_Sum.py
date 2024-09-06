class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        ans = defaultdict(int)
        ans[0] = 0
        pre = 0

        for i in range(len(nums)):
            pre += nums[i]
            if pre % k not in ans: ans[pre % k] = i + 1
            else:
                if ans[pre % k] < i: return True

        return False
