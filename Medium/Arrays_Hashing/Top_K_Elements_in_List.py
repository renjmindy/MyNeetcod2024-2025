class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cp = Counter(nums)

        sp = sorted(cp.items(), key = lambda x:x[1], reverse=True)[:k]

        print(sp)

        return [k for k, v in sp]
