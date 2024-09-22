class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0

        while l <= r:
            pre = people[l] + people[r]
            if pre <= limit: l += 1
            r -= 1
            ans += 1

        return ans
