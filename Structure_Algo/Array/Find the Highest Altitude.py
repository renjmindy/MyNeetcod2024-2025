class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        ans = [0]
        pre = 0

        for r in range(len(gain)):
            pre += gain[r]
            ans.append(pre)

        return max(ans)
