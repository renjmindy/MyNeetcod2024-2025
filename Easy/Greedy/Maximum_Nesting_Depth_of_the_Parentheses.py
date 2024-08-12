class Solution:
    def maxDepth(self, s: str) -> int:
        
        ans, cnt = 0, 0
        mp = list()

        for c in s: 
            if c == '(': 
                mp.append(c)
                cnt += 1
                ans = max(ans, cnt) 
            elif c == ')':
                if mp[-1] == '(': 
                    mp.pop()
                    cnt -= 1

        return ans
