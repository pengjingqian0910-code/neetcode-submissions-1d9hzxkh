class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if(prices[l] > prices[r]):
                l = r
            elif(prices[l] < prices[r]):
                 curr = prices[r] - prices[l]
                 max_profit = max(max_profit, curr)
            r += 1
        return max_profit
            
        