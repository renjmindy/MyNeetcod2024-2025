from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for str in strs:
            mp[''.join(sorted(str))].append(str)

        return list(mp.values())
