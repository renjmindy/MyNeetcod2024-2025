class Solution:
    def numberOfWays(self, s: str) -> int:
        
        ones = Counter(s)['1']
        zeros = Counter(s)['0']

        ans, cnt_ones, cnt_zeros = 0, 0, 0

        for r in range(len(s)):
            if s[r] == '0':
                ans += cnt_ones * (ones - cnt_ones)
                cnt_zeros += 1
            if s[r] == '1':
                ans += cnt_zeros * (zeros - cnt_zeros)
                cnt_ones += 1

        return ans
