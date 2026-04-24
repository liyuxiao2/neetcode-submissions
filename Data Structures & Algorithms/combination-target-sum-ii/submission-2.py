class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, cur_sum):
            if cur_sum == target and cur not in res:
                res.append(cur.copy())
                return
            if i >= len(candidates) or cur_sum > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, cur_sum + candidates[i])

            cur.pop()
            dfs(i + 1, cur, cur_sum)
        
        dfs(0, [], 0)

        return res
        
        dfs(0)

        return res