class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #iterate through the 2d array, once we see the first char of the word we can do DFS

        #we mark our current position, and search L, R, U, D (considering boundaries)

        #seen values should onmly persist within the current DFS

        #we append to the stack if the neighbors match the next word

        #we continue to DFS until we reach the end of the word

        #else we continue to loop, if we reach the end return False

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(row, col, i = 0):
            if i == len(word):
                return True
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or board[row][col] != word[i] or visited[row][col] == True:
                return False
            
            visited[row][col] = True

            res = (dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1))
                

            visited[row][col] = False
            return res


        for j in range(len(board)):
            for k in range(len(board[0])):
                if dfs(j, k):
                    return True
        return False
