class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        cache = {}

        #we can choose to add it to subset 1, or leave it

        def dfs(i, cur_s):
            if i == len(nums):
                return False
            if cur_s == target:
                cache[i] = True
                return True
            
            
            cache[i] = dfs(i + 1, cur_s + nums[i]) or dfs(i + 1, cur_s)

            return cache[i]
        

        return dfs(0, 0)

