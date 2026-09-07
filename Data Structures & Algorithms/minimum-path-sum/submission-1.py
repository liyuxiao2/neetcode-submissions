class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}

        def dfs(i, j):
            if i == len(grid) or j == len(grid[0]):
                return float("inf")
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if (i, j) in dp:
                return dp[(i, j)]

            res = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))

            dp[(i, j)] = res
            return res
        
        
        
        return dfs(0,0)


            