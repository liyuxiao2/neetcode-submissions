class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums): #we reached a leaf node
                res.append(subset.copy())
                return
            

            #decision to include nums[i]

            subset.append(nums[i])
            dfs(i + 1)

            #left branch


            #decision not to include nums[i]
            #remove the value we just added, the other decision
            subset.pop()
            dfs(i + 1)
        
        dfs(0)

        return res