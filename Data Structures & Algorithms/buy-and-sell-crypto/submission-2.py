class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case
        if len(prices) == 1 or len(prices) == 0:
            return 0
        
        # iteration
        min_price, curr_profit = float('inf'), 0
        for todays_price in prices:
            min_price = min(min_price, todays_price)
            curr_profit = max(todays_price - min_price, curr_profit)
        
        # return 
        return int(curr_profit)