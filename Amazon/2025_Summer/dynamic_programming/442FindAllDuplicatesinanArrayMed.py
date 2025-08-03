class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        mp = defaultdict(int)

        ans = list()

        for num in nums: mp[num] += 1

        for k, v in mp.items():
            if v > 1: ans.append(k)

        return ans
