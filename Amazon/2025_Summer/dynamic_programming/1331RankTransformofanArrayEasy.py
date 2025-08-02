class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        b = list(set(arr))
        b.sort()

        mp = defaultdict(int)

        for i, j in enumerate(b):
            mp[j] = i + 1

        return [mp[a] for a in arr]
