# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        #get heights of left and right

        def dfs(root):
            nonlocal res
            #base case
            if root == None:
                return 0

            #get max h of r
            r = dfs(root.right)
            #get max h of l
            l = dfs(root.left)
            res = max(res, l+r)

            return 1 + max(l, r)
        
        dfs(root)
        return res
