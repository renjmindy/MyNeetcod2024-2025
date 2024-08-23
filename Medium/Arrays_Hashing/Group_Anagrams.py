class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        for str_item in strs:
            ans[''.join(sorted(list(str_item)))].append(str_item)

        return list(ans.values())
