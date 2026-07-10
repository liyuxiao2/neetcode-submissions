class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i):
            if i <= n:
                if len(cur) == k:
                    res.append(cur.copy())
                    return
                
                cur.append(i+1)
                dfs(i+1)

                cur.pop()
                dfs(i+1)
            else:
                return
        
        dfs(0)

        return res