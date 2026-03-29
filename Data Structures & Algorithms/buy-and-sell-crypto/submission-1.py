class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,max_profit = 0,0
        while (left<len(prices)) :
            right = len(prices) - 1 
            while right >= left:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
                right -= 1 
            left += 1
        return max_profit
                

            
             
            