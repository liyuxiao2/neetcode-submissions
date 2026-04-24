class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        total = 0

        def bfs(i, j):
            q = [[i, j]]

            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

            while q:
                r, c = q.pop()

                for d in directions:
                    new_r, new_c = r + d[0], c + d[1]

                    if(0 <= new_r < rows and 0 <= new_c < cols and
                        grid[new_r][new_c] == "1" and 
                        (new_r, new_c) not in visited):
                            visited.add((new_r, new_c))
                            q.append([new_r, new_c])
    

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    total += 1
                    bfs(i, j)
        
        return total



