class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #choice to continue down j + 1, or just by j

        #we break once we hit i == len(triangle) or j == len(triagnel[0])

        row = len(triangle)

        dp = {}

        def dfs(i, j):
            if i == row:
                return 0
            if (i , j) in dp:
                return dp[(i, j)]
            
            res = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))

            dp[(i, j)] = res

            return res
        
        
        return dfs(0, 0)

