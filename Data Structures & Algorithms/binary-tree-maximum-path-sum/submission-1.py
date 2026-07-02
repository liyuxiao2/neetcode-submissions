# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        cur_s = [root.val]


        def dfs(r):
            if not r:
                return 0
            
            #traverse left and right subtrees
            left = dfs(r.left)
            right = dfs(r.right)

            l_max = max(left, 0)
            r_max = max(right, 0)

            print(l_max, r_max)

            cur_s[0] = max(cur_s[0], r.val + l_max + r_max)

            return r.val + max(l_max, r_max)
        
        dfs(root)

        return cur_s[0]