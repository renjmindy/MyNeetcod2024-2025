class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        wstring = ''.join(words)

        cstring = Counter(wstring)

        for k, v in cstring.items():
            if v % len(words) != 0: return False

        return True
