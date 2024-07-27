class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        if 0 in nums: return 0
        ans = list()

        for num in nums:
            if num > 0: ans.append(1)
            else: ans.append(-1)

        return 1 if Counter(ans)[-1] % 2 == 0 else -1
