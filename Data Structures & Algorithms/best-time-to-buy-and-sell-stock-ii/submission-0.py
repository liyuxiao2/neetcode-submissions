class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #choose to buy or not buy and sell or not sell

        dp = {}

        def dfs(i, is_hold):
            if i >= len(prices):
                return 0
            if (i, is_hold) in dp:
                return dp[(i, is_hold)]

            if is_hold:
                res = max(dfs(i + 1, False) + prices[i], dfs(i + 1, True))
            else:
                res = max(dfs(i + 1, True) - prices[i], dfs(i + 1, False))
            
            dp[(i, is_hold)] = res
            return res
        
        return dfs(0, False)