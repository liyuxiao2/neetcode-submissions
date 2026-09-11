class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(m - 1, n - 1): 1}

        def dfs(i, j):
            if i > m:
                return 0
            if j > n: 
                return 0
            if (i, j) in dp:
                return dp[(i,j)]

            res = 0

            res += dfs(i + 1, j) + dfs(i, j + 1)

            dp[(i,j)] = res

            return res
        
        return dfs(0,0)
