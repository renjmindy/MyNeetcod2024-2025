class Solution:
    def reorganizeString(self, s: str) -> str:
        
        s_sorted = sorted(sorted(s), key=s.count, reverse=True)

        mid = math.ceil(len(s_sorted) / 2)

        s_sorted[::2], s_sorted[1::2] = s_sorted[:mid], s_sorted[mid:]

        return ''.join(s_sorted) if len(s_sorted) == 1 or s_sorted[0] != s_sorted[1] else ''
