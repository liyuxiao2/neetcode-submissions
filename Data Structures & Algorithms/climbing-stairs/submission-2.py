class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in cache:
                return cache[i]
            
            temp = dfs(i + 1) + dfs(i + 2)

            cache[i] = temp

            return cache[i]
        
        return dfs(0)
            
            