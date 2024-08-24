class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(str_item)) + '/' + str_item for str_item in strs) 

    def decode(self, s: str) -> List[str]:
        
        l, ans = 0, list()

        while l < len(s):
            r = l
            while s[r] != '/': r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            ans.append(s[l:r])
            l = r

        return ans
