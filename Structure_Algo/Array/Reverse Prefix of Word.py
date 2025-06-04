class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if ch not in word: return word

        l, r = 0, 0

        alist = list(word)

        while r < len(alist) and alist[r] != ch:
            r += 1
        while l < r:
            alist[l], alist[r] = alist[r], alist[l]
            l += 1
            r -= 1

        return ''.join(alist)
