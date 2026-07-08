class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(total, i):
            cur_t = 0
            if i == len(nums):
                return total
            
            cur_t += dfs(total ^ nums[i], i + 1)

            cur_t += dfs(total, i + 1)

            return cur_t
        
        return(dfs(0, 0))
        
            
            