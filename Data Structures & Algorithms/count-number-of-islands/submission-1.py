class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row, col = len(grid), len(grid[0])
        def bfs(i, j):

            q = deque()
    
            q.append((i,j))
            grid[i][j] = "-1"

            while q:
                i, j = q.popleft()

                directions = [(-1, 0), (1,0), (0, 1), (0, -1)]

                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if (0 <= x < row) and (0 <= y < col) and grid[x][y] == "1":
                        q.append((x, y))
                        grid[x][y] = "-1" #mark as seen 
            
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)
        return count