class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        cp = Counter(nums)
        mc = cp.most_common()
        #print(mc)
        ans = [[] for _ in range(mc[0][1])]

        for num, cnt in mc:
            for c in range(cnt):
                ans[c].append(num)

        return ans
