class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)

        l, cnt, ans = 0, 0, 0

        for r in range(len(s)):
            mp[s[r]] += 1

            cnt = max(cnt, mp[s[r]])

            while r - l + 1 - cnt > k:
                mp[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
