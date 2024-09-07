class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        ans = [0] * len(dominoes)
        force = 0

        for l in range(len(dominoes)):
            if dominoes[l] == 'R': force = len(dominoes)
            elif dominoes[l] == 'L': force = 0
            else: force = max(force - 1, 0)
            ans[l] += force

        force = 0
        for r in range(len(dominoes) - 1, -1, -1):
            if dominoes[r] == 'R': force = 0
            elif dominoes[r] == 'L': force = len(dominoes)
            else: force = max(force - 1, 0)
            ans[r] -= force

        return ''.join(['.' if net == 0 else 'R' if net > 0 else 'L' for net in ans])
        
