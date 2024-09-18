class Solution:
    def frequencySort(self, s: str) -> str:
        
        cp = Counter(s)
        sp = sorted(cp.items(), key = lambda x:x[1], reverse=True)

        ans = ''

        for k, v in sp:
            for i in range(v): ans += k

        return ans

class Solution:
    def frequencySort(self, s: str) -> str:
        
        cp = Counter(s)
        sp = dict(sorted(cp.items(), key = lambda x:x[1], reverse=True))

        ans = ''

        for k, v in sp.items():
            for i in range(v): ans += k

        return ans
