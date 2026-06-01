class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        [["O","O","O","O","X","X"],
        ["O","O","O","O","O","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","X","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","O","O"]]
        """

        #its surrounded if its surrounded by 4 X's or seen values
        row, col = len(board), len(board[0])
        seen = set()

        def in_bounds(i, j):
            return 0 <= i < row and 0 <= j < col

        def bfs(i, j):
            q = deque()
            q.append((i,j))
            directions = [(0, 1), (1,0), (-1, 0), (0, -1)]
            to_mark = []
            is_surrounded = True

            while q:
                x, y = q.popleft()
                to_mark.append((x,y))

                if x == 0 or x == row - 1 or y == 0 or y == col - 1:
                    is_surrounded = False

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if in_bounds(new_x, new_y) and board[new_x][new_y] == "O" and (new_x, new_y) not in seen:
                        q.append((new_x, new_y))
                        seen.add((new_x, new_y))
            
            if is_surrounded:
                for r, c in to_mark:
                    board[r][c] = "X"

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i,j) not in seen:
                    seen.add((i, j))
                    bfs(i, j)