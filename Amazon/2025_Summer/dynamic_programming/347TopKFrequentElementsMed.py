class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = Counter(nums)

        ans = list()

        mp_sorted = sorted(mp.items(), key = lambda x:x[1], reverse=True)[:k]

        return list(k for k, v in mp_sorted)
