class Solution:
    def minSwaps(self, s: str) -> int:
        
        ans = list()

        for c in s:
            if c == '[': ans.append(c)
            else:
                if ans: ans.pop()

        return (len(ans) + 1) // 2
