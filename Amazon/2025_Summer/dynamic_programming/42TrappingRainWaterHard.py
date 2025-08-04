# 135. Candy (Hard)

class Solution:
    def trap(self, height: List[int]) -> int:
        
        mpl, mpr = [0] * len(height), [0] * len(height)
        mpl[0] = height[0]
        mpr[len(height) - 1] = height[len(height) - 1]

        ans = 0

        for l in range(1, len(height)):
            mpl[l] = max(mpl[l - 1], height[l])

        for r in range(len(height) - 2, -1, -1):
            mpr[r] = max(mpr[r + 1], height[r])

        for i in range(1, len(height) - 1):
            ans += min(mpl[i], mpr[i]) - height[i]

        return ans
