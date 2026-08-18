class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we just check if the target is greater than the last elem of the row, we can bsearch on the end 
        #toral of m rows

        t, b = 0, len(matrix) - 1
        row = 0


        while t <= b:
            m = (t + b) // 2

            if matrix[m][-1] >= target and matrix[m][0] <= target:
                row = m
                break
            elif matrix[m][-1] < target:
                t = m + 1
            elif matrix[m][0] > target:
                b = m - 1
            
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False
