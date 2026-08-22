class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        # {0 : , 1: , 2:, }

        def dfs(i, c_sum):
            if i == len(nums):
                return 1 if c_sum == target else 0
            
            if (i, c_sum) in dp:
                return dp[(i, c_sum)]
            
            res = dfs(i + 1, c_sum - nums[i]) + dfs(i + 1, c_sum + nums[i])

            dp[(i, c_sum)] = res
            return res
        
        
        r = dfs(0, 0)
        return r