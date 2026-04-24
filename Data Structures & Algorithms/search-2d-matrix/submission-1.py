class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if(matrix[i][-1] < target):
                continue


            l, r = 0, len(matrix[i])-1

            while(l <= r):
                middle = int((l+r) / 2)
                if(matrix[i][middle] == target):
                    return True
                elif(matrix[i][middle] > target):
                    r = middle - 1
                else:
                    l = middle + 1
        return False