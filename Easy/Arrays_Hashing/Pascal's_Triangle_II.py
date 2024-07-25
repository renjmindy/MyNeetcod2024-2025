class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = list()

        for r in range(rowIndex + 1):
            tmp = list()
            for l in range(r + 1):
                if l == 0 or l == r:
                    tmp.append(1)
                else:
                    tmp.append(ans[r-1][l-1] + ans[r-1][l])

            ans.append(tmp)

        return ans[-1]
