class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #what we do is use the regular subsets algorithim

        #sort the array first, and we just check if the current subset is already in the result we can skip
        #else we add it to the res

        res = []
        cur = []
        nums.sort()

        def dfs(i):
            if(i >= len(nums)):
                if cur not in res:
                    res.append(cur.copy())
                return

            
            cur.append(nums[i])
            dfs(i + 1)

            cur.pop()
            dfs(i + 1)
        
        dfs(0)

        return res