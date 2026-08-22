class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if we sell, we cant buy i + 1 (move i + 2)

        #we can only hold 1

        #we can decide to buy or not buy a coin, if we buy we have
        dp = defaultdict(int)

        def dfs(i, holding):
            print(i)
            if i >= len(prices):
                return 0
            if (i, holding) in dp:
                return dp[(i, holding)]
            
            if holding:
                res = max(prices[i] + dfs(i + 2, False), dfs(i + 1, True))
            else:
                res = max(-prices[i] + dfs(i + 1, True), dfs(i + 1, False))

            dp[(i, holding)] = res
            return res
        
        return dfs(0, False)


