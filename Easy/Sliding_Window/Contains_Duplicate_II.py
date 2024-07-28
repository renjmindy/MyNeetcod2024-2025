class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        mp = defaultdict(int)

        for r in range(len(nums)):
            if nums[r] in mp:
                if r - mp[nums[r]] <= k: return True
            mp[nums[r]] = r 
             
            
        return False
