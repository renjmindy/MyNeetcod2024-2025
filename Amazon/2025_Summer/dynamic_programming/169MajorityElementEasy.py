class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mp = Counter(nums)

        mp_sorted = sorted(mp.items(), key = lambda x:x[1], reverse=True)[:1]

        return mp_sorted[0][0]
