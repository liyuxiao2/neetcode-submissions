class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        max_perim = 0
        row, col = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        seen = set() 



        def dfs(x, y):           
            perim = 0
            stack = [(x,y)]
            seen.add((x,y))

            while stack:
                x, y = stack.pop()

                for d in directions:
                    dx, dy = d

                    new_x, new_y = x + dx, y + dy

                    if not (0 <= new_x < row and 0 <= new_y < col) or grid[new_x][new_y] == 0:
                        perim += 1
                    elif (new_x, new_y) not in seen and grid[new_x][new_y] == 1:
                        stack.append((new_x, new_y))
                        seen.add((new_x,new_y))

            return perim

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in seen:
                    max_perim = max(max_perim, dfs(i, j))
        return max_perim
                    
