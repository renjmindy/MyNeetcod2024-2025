class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            if height[l] < height[r]:
                ans = max(ans, height[l] * (r - l))
                l += 1
            elif height[l] > height[r]:
                ans = max(ans, height[r] * (r - l))
                r -= 1
            else:
                ans = max(ans, height[r] * (r - l))
                r -= 1
                l += 1

        return ans 
