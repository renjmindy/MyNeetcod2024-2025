class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        l, r = 0, len(s) - 1

        alist = list(s)

        #print(alist)

        while l < r:
            if alist[l].isalpha() and alist[r].isalpha():
                alist[l], alist[r] = alist[r], alist[l]
                r -= 1
                l += 1
            elif not alist[r].isalpha(): r -= 1
            else: l += 1

        return ''.join(alist)
