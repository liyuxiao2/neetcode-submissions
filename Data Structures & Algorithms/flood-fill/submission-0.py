class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src = image[sr][sc]

        def dfs(i, j):
            print(image)
            if not (0 <= i < len(image) and 0 <= j < len(image[0])) or image[i][j] != src:
                return
            if image[i][j] == color:
                return
            
            image[i][j] = color

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        dfs(sr, sc)

        return image