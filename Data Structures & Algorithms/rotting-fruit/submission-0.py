class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        #the tricky part is when you have multiple rotten fruit how 
        #fast does everything become rotten?
        q = collections.deque()
        time, fresh = 0, 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while q and fresh > 0:
            level = len(q)
            for _ in range(level):
                i, j = q.popleft()

                for d in directions:
                    new_r, new_c = i + d[0], j + d[1]

                    if(0 <= new_r < rows and 0 <= new_c < cols
                        and grid[new_r][new_c] == 1):
                            fresh -= 1
                            grid[new_r][new_c] = 2
                            q.append((new_r, new_c))
            time += 1
        
        if(fresh > 0):
            return - 1
            
        return time

            


