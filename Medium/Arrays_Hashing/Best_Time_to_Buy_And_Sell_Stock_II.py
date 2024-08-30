class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, ans = 0, 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]: ans += prices[r] - prices[l]
            l += 1

        return ans
