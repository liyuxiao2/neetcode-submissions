class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_count = 0

        def bfs(r, c):
            q = collections.deque()
            count = 0

            visited.add((r, c))
            q.append((r,c))
            count += 1

            directions = [[1,0], [-1,0], [0,1], [0, -1]]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc

                    if (new_r in range(rows) and new_c in range(cols) and
                        grid[new_r][new_c] == 1 and
                        (new_r, new_c) not in visited):
                            visited.add((new_r,new_c))
                            q.append((new_r,new_c))
                            count += 1
            return count
            
        

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1:
                    count = bfs(i, j)
                    max_count = max(max_count, count)
        
        return max_count

