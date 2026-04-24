class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_low = prices[0]

        for i in range(len(prices)):
            if buy_low > prices[i]:
                buy_low = prices[i]
            
            if(profit < (prices[i]-buy_low)):
                profit = prices[i]-buy_low
        
        return profit