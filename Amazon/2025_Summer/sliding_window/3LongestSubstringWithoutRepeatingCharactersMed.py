class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        l, ans = 0, 0

        for r in range(len(s)):
            mp[s[r]] += 1

            while mp[s[r]] == 2: # till the removel of repeating character
                mp[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
