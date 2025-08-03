class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
        l, cnt, mp = 0, 0, set()

        for r in range(len(nums)):
            if nums[r] % p == 0: cnt += 1

            while cnt > k:
                if nums[l] % p == 0: cnt -= 1
                l += 1

            ans = nums[l:r + 1]
            #print(ans)

            for i in range(len(ans)):
                #print(tuple(ans[i:]))
                mp.add(tuple(ans[i:]))

        return len(mp)
