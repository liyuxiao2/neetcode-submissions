class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 2 dimensions (coordinate pair, prev element)
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])

        dp = {}
        directions = [(0, 1), (1,0), (0,-1), (-1, 0)]

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            res = 1

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ni, nj))
            
            dp[(i, j)] = res
            return res

        return max(dfs(i, j) for i in range(rows) for j in range(cols))


