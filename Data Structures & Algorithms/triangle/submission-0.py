class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #choice to continue down j + 1, or just by j

        #we break once we hit i == len(triangle) or j == len(triagnel[0])

        row, col = len(triangle), len(triangle[0])

        min_t = float("inf")

        dp = {}

        def dfs(i, j):
            if i == row:
                return 0
            if (i , j) in dp:
                return dp[(i, j)]
            
            res = min(triangle[i][j] + dfs(i + 1, j), triangle[i][j] + dfs(i + 1, j + 1))

            dp[(i, j)] = res

            return res
        
        
        return dfs(0, 0)

