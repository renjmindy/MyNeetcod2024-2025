class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        buy_mp, sell_mp = [0] * len(prices), [0] * len(prices)

        buy_mp[0] = -prices[0]
        sell_mp[0] = 0

        for i in range(k):
            buy_mp[0] = -prices[0]
            for r in range(1, len(prices)):
                buy_mp[r] = max(buy_mp[r - 1], sell_mp[r] - prices[r])
                sell_mp[r] = max(sell_mp[r - 1], buy_mp[r] + prices[r])

        
        return sell_mp[-1]
