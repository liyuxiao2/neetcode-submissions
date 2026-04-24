class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        #we can bfs over this

        #we only bfs nodes that are inf

        #essentially we bfs at every land node, and since BFS will guarantee to provide us the
        #SSP, we can return the count at that point once we find 0
        #if we never find a 0, and the q is empty (i.e we can no longer traverse) dont mod

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j, 0))
            visited = [] #we dont want to go in an infinite cycle this can happen

            while q:
                row, col, count = q.popleft()

                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for d in directions:
                    new_r, new_c = row + d[0], col + d[1]

                    if(0 <= new_r < rows and 0 <= new_c < cols 
                        and (new_r, new_c) not in visited
                        and (grid[new_r][new_c] != -1)):
                            if(grid[new_r][new_c] == 0):
                                return (count + 1)
                            else:
                                visited.append((new_r, new_c))
                                q.append((new_r, new_c, count + 1))

            return -1 #we never found shortest path
        
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 2147483647):
                    value = bfs(i, j)
                    if value != -1:
                        grid[i][j] = value


