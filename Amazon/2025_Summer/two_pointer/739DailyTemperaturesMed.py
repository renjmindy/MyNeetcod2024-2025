class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = list()

        ans = [0] * len(temperatures)

        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                idx = stack.pop()
                ans[idx] = (r - idx)
            stack.append(r)

        return ans
