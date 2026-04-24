# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #i think we can just dfs down

        #so the optimal solution is dfs i was just thinking about it wrong

        #we set global count and result

        #we dfs to the bottom, then we subtract by 1

        #if the count is 0 then we know were at the right spot

        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res

            if not node:
                return 
            
            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                res = node.val
                
            dfs(node.right)
        
        dfs(root)

        return res
