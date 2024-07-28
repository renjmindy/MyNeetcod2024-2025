class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, ans = 0, 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                ans = max(ans, prices[r] - prices[l])
            else:
                l = r

        return ans
