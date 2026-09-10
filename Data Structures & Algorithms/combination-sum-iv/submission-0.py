class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        dp = {0: 1}

        def dfs(sums):
            if sums in dp:
                return dp[sums]
            
            res = 0

            for i in range(len(nums)):
                if sums < nums[i]:
                    break
                res += dfs(sums - nums[i])
            
            dp[sums] = res
            return res
        
        return dfs(target)