class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: sign = -1
        else: sign = 1
            
        x *= sign
            
        xlist = list(str(x))
        
        l, r = 0, len(xlist) - 1
        
        while l < r:
            xlist[l], xlist[r] = xlist[r], xlist[l]; l += 1; r -= 1
                
        #print(xlist)
                
        return int(''.join(xlist)) * sign if int(''.join(xlist)) * sign >= -(2**31) and int(''.join(xlist)) * sign <= (2**31 - 1) else 0
