class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return
            
            for i in range(len(nums)):
                if nums[i] != float("inf"):
                    val = nums[i]
                    perm.append(val)
                    nums[i] = float("inf")

                    dfs(perm)

                    nums[i] = val
                    perm.pop()

                

        
        dfs([])
        return list(res)
