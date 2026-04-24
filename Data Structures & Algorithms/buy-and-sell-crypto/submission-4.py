class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])


            if(prices[r] <= prices[l]):
                l = r
            
            r += 1
        
        return profit
        # profit = 0
        # buy_low = prices[0]

        # for i in range(len(prices)):
        #     if buy_low > prices[i]:
        #         buy_low = prices[i]
            
        #     if(profit < (prices[i]-buy_low)):
        #         profit = prices[i]-buy_low
        
        # return profit