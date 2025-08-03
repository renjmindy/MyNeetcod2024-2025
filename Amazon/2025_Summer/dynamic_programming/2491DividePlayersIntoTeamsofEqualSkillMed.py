class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        ans = 0

        for r in range(len(skill) // 2):
            if skill[r] + skill[len(skill) - r - 1] != skill[0] + skill[-1]: return -1
            ans += skill[r] * skill[len(skill) - r - 1]

        return ans
