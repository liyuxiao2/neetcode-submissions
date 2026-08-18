class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rows become columns
        # first row -> last column
        # last column -> first row
        """
        Input: matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]


        revresed = [
            [7,8,9]
            [4,5,6],
            [1,2,3],
        ]
        """
        matrix.reverse()




        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        