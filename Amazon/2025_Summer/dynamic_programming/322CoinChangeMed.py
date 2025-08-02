class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        mp = [math.inf] * (amount + 1)
        mp[0] = 0

        for r in range(1, amount + 1):
            for coin in coins:
                if r >= coin:
                    mp[r] = min(mp[r], 1 + mp[r - coin])

        return mp[amount] if mp[amount] < math.inf else -1
