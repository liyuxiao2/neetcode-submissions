class Solution:
    def numSquares(self, n: int) -> int:
        dp = {0: 0}

        def dfs(target):
            if target < 0:
                return n + 1
            if target in dp:
                return dp[target]
            
            res = n + 1
            max_square_root = int(math.sqrt(target))
            for i in range(max_square_root, 0, -1):
                res = min(res, 1 + dfs(target - (i ** 2)))

            dp[target] = res
            return res
        return dfs(n)
            