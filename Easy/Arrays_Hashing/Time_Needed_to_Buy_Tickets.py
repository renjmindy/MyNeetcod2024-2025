class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        ans = 0

        for r in range(len(tickets)):
            if r <= k:
                ans += min(tickets[r], tickets[k])
            else:
                ans += min(tickets[r], tickets[k] - 1)

        return ans
