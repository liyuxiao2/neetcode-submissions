class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, sums, cur):
            if i == len(nums) or sums >= target:
                if sums == target:
                    res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i, sums + nums[i], cur)

            cur.pop()
            dfs(i+1, sums, cur)
        
        dfs(0, 0, cur)

        return res