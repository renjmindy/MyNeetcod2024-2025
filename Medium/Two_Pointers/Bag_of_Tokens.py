class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        l, r = 0, len(tokens) - 1
        ans, scr = 0, 0

        while l <= r:
            if tokens[l] <= power: 
                power -= tokens[l]
                scr += 1
                l += 1
                ans = max(ans, scr)
            elif scr > 0:
                power += tokens[r]
                scr -= 1
                r -= 1
            else:
                break

        return ans
