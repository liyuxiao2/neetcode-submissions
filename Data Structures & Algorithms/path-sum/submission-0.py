# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, cur_s):
            if not node:
                return False
            

            cur_s += node.val

            if not node.left and not node.right:
                return cur_s == targetSum
            
            return dfs(node.left, cur_s) or dfs(node.right, cur_s)
        
        return dfs(root, 0)