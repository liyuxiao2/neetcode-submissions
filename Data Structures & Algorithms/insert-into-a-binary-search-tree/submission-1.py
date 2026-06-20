# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        tmp = root

        while True:
            if tmp.val < val:
                if not tmp.right:
                    tmp.right = TreeNode(val)
                    return root
                tmp = tmp.right
            else:
                if not tmp.left:
                    tmp.left = TreeNode(val)
                    return root
                tmp = tmp.left