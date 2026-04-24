class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(len(board)):
            valid_board = set()
            for j in range(len(board[i])):
                if board[i][j] in valid_board and (board[i][j] != "."):
                    return False
                valid_board.add(board[i][j])
        #check columns
        for i in range(len(board)):
            valid_board = set()
            for j in range(len(board[i])):
                if board[j][i] in valid_board and (board[j][i] != "."):
                    return False
                valid_board.add(board[j][i])
        #check grids
        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                valid_board = set()
                for w in range(3):
                    for x in range(3):
                        if board[i+w][j+x] in valid_board and (board[i+w][j+x] != "."):
                            return False
                        valid_board.add(board[i+w][j+x])
        return True
         