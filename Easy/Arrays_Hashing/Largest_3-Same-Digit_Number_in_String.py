class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        ans = ''

        for r in range(len(num) - 2):
            if len(set(num[r:r+3])) == 1:
                if len(ans) > 0: 
                    if int(num[r:r+3]) > int(ans): ans = num[r:r+3]
                else: ans = num[r:r+3]
        return ans
