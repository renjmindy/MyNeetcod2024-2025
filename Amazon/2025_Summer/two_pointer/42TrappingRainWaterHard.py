class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0
        stack = list()

        for r in range(len(height)):
            while stack and height[stack[-1]] < height[r]:
                mid = stack.pop()
                if not stack: break
                l = stack[-1]
                minH = min(height[r] - height[mid], height[l] - height[mid])
                ans += minH * (r - l - 1)
            stack.append(r)

        return ans
