class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        ans = [0] * (n + 1)

        for people in trust:
            ans[people[0]] -= 1
            ans[people[1]] += 1

        for i in range(1, n + 1):
            if ans[i] == n - 1: return i

        return -1 
