# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # you would dfs down each path, once you find a node that hits, we bubble back up
        # same with the other node, we would bubble back up until we see a node that is already true
        # the first node we see that is true, we return that node
        if p.val > q.val:
            p, q = q, p

        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            print(root.val)
            return root