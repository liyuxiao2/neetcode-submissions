# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #cur max as we dfs, if we see that our current node > than cur_max, + 1 to res, and update cur max
        def dfs(root, cur_max):
            if not root:
                return 0
            
            res = 0

            if root.val >= cur_max:
                res += 1
                cur_max = root.val
            
            res += dfs(root.left, cur_max) + dfs(root.right, cur_max)

            return res
        
        return dfs(root, float("-inf"))