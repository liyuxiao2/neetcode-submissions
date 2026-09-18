class Solution:
    def integerBreak(self, n: int) -> int:
        res = 0
        dp = {0: 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 0 if i == n else i

            for k in range(1, i):
                res = max(k * dfs(i - k), res)
            
            dp[i] = res
            return res
        
        return dfs(n)