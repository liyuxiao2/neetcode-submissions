# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 1

        def dfs(node, cur_max):
            nonlocal cnt

            if not node:
                return
            
            if node.val >= cur_max:
                cnt += 1
                cur_max = node.val
            
            dfs(node.right, cur_max)
            dfs(node.left, cur_max)
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return cnt