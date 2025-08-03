class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        mp = defaultdict(int)
        

        for r in range(len(arr)):
            mp[arr[r] % k] += 1

        if mp[0] % 2: return False

        for key, v in mp.items():
            if mp[key] != mp[(k - key) % k]: return False

        return True
