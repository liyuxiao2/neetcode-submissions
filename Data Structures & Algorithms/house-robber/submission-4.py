class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i >= len(nums):
                return 0
                
            if i in cache:
                return cache[i]

            v1 = dfs(i + 1) if i + 1 < len(nums) else 0
            v2 = nums[i] + dfs(i + 2) if i + 2 < len(nums) else nums[i]
            
            cache[i] = max(v1, v2)

            return cache[i]
        
        return dfs(0)

        