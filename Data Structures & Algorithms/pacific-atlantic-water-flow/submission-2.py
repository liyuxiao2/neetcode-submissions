class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, ocean, prevH):
            if ((i,j) in ocean or 
                i < 0 or j < 0 or
                i == ROW or j == COL or
                heights[i][j] < prevH
            ):
                return
            
            ocean.add((i,j))

            newH = heights[i][j]

            dfs(i + 1, j, ocean, newH)
            dfs(i - 1, j, ocean, newH)
            dfs(i, j + 1, ocean, newH)
            dfs(i, j - 1, ocean, newH)
        
        for j in range(COL):
            dfs(0, j, pacific, heights[0][j])
            dfs(ROW - 1, j, atlantic,  heights[ROW - 1][j])
        
        for i in range(ROW):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, COL - 1, atlantic, heights[i][COL - 1])

        return [[i,j] for i, j in (atlantic & pacific)]
            