class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        mp = Counter(s)

        for key, v in mp.items():
            if v < k:
                return max([self.longestSubstring(c, k) for c in s.split(key)]) # split is to skip shorter length of character

        return len(s)
