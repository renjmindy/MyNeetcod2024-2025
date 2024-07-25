class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        plist = list(pattern)
        slist = s.split()

        if len(plist) != len(slist): return False

        return len(set(plist)) == len(set(slist)) == len(set(zip(plist, slist)))
