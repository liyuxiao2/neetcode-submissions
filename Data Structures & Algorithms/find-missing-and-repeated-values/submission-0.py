class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        repeated = set()


        res = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in repeated:
                    res.append(grid[i][j])
                else:
                    repeated.add(grid[i][j])


        for i in range(1, len(grid) * len(grid[0]) + 1):
            if i not in repeated:
                res.append(i)
                return res
                
        return res
