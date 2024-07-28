class Solution:
    def reverseWords(self, s: str) -> str:
        
        slist = s.split(' ')
        ans = list()

        for word in slist:
            ans.append(word[::-1])

        return ' '.join(ans) 
