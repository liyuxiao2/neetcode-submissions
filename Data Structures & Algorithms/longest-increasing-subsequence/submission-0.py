class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, prev):
            if i == len(nums):
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            res = dfs(i + 1, prev)

            if prev == -1 or nums[prev] < nums[i]:
                res = max(res, 1 + dfs(i + 1, i))

            
            cache[(i, prev)] = res
            
            return res
        
        return dfs(0, -1)



            