# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        #we would store the info like this

        # (node, current_max = -inf, cur_count)

        # increase cur_count if node.val > cur_max
        # update cur max like this cur_max = max(cur_max, node.val)
        # if false, then we know that node.val < cur_max, continue


        return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)


    

    def dfs(self, root, max_val):
        count = 0

        if not root:
            return 0
        
        if(root.val >= max_val):
            max_val = root.val
            count = 1
        
        return count + self.dfs(root.left, max_val) + self.dfs(root.right, max_val)

 