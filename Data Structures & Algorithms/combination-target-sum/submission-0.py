class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, cur, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or cur_sum > target:
                return

            cur.append(nums[i])
            dfs(i, cur, cur_sum + nums[i])

            cur.pop()
            dfs(i + 1, cur, cur_sum)
        
        dfs(0, [], 0)

        return res


            