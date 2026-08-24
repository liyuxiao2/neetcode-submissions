class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 2 dimensions, are index s, and index at t

        #the base case is if we reach the end of s, we return 0

        #if we reach the end of t (that means everything matches) we can return 1 (indicating we got 1)

        #at every position we can either choose s or not choose the char of s

        dp = {}

        def dfs(i , j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            dp[(i,  j)] = res

            return res
        
        return dfs(0, 0)

            