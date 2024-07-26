class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        x, y = 0, 0
        ans = list()
        ans.append((x, y))

        for p in path:
            if p == 'N': y += 1
            elif p == 'S': y -= 1
            elif p == 'E': x += 1
            else: x -= 1
            ans.append((x, y))

        return len(ans) > len(set(ans))
