class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                tmp1 = s[:l] + s[l + 1:]
                tmp2 = s[:r] + s[r + 1:]
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
            l += 1
            r -= 1

        return True
