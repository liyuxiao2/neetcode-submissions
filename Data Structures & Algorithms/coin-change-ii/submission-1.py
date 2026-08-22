class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, cur_a):
            if i >= len(coins):
                return 0
            if cur_a >= amount:
                return 1 if cur_a == amount else 0
            if (i, cur_a) in dp:
                return dp[(i, cur_a)]
            
            res = dfs(i + 1, cur_a) + dfs(i, cur_a + coins[i])

            dp[(i, cur_a)] = res

            return res

        return dfs(0, 0)
                