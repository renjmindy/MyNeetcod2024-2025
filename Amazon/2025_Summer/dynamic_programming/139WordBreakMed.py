
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordset = set(wordDict)

        mp = [False] * (len(s) + 1)

        mp[0] = True

        for r in range(1, len(s) + 1):
            for l in range(r):
                if mp[l] == True and s[l:r] in wordset: mp[r] = True; break

        return mp[-1]
