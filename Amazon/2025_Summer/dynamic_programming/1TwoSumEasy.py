class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mp = defaultdict(int)
        ans = list()
        
        for r in range(len(nums)):
            if target - nums[r] in mp:
                ans.append(mp[target - nums[r]])
                ans.append(r)
            mp[nums[r]] = r
            
        return ans
