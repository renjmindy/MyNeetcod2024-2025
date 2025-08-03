class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, ans = 0, 0

        for r in range(1, len(prices)):
            buy = prices[l]
            sell = prices[r]

            if sell > buy: ans += sell - buy

            l += 1

        return ans
