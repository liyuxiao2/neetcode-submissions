class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #remove, we either skip i or j
        #replace, we move i and j together
        #insert, we will skip i or j again (either one)

        dp = {}

        def dfs(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1) and not (j == len(word2)):
                return len(word2) - j
            if not (i == len(word1)) and j == len(word2):
                return len(word1) - i
            if (i, j) in dp:
                return dp[(i, j)]

            res = float("inf")
            if word1[i] == word2[j]:
                res = min(res, dfs(i + 1, j + 1))
            if word1[i] != word2[j]:
                res = min(res, 1 + dfs(i + 1, j + 1), 1 + dfs(i +1 , j), 1 + dfs(i, j + 1))
            
            dp[(i, j)] = res
            
            return res
        
        v = (dfs(0, 0))
        print(dp)
        return v