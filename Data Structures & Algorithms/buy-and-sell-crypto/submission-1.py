class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 2, -1, -1):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    x = prices[j] - prices[i]
                    profit = max(x, profit)
        return profit