class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        mp = defaultdict(int)
        ans = 0

        for r in range(len(time)):
            if (60 - (time[r] % 60)) % 60 in mp: ans += mp[(60 - (time[r] % 60)) % 60]
            mp[time[r] % 60] += 1 

        return ans
