class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = list()
        ans.append(0)

        for i in range(1, n + 1):
            if i % 2:
                ans.append(ans[i - 1] + 1)
            else:
                ans.append(ans[i // 2])

        return ans
