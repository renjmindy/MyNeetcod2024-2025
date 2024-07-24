class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''

        strs.sort()

        for r in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][r] == strs[-1][r]: ans += strs[0][r]
            else: return ans

        return ans
