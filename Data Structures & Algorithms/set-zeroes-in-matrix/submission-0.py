class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #if we see a zero, zero the entire column, and row, and then skip iterating on that row     
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows[i], cols[j] = True, True



        for i in range(ROWS):
            for j in range(COLS):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
        

        