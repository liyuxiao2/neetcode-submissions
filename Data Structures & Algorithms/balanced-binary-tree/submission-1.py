# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        right = self.maxDepth(root.right) + 1
        left = self.maxDepth(root.left) + 1

        return (abs(left - right) <= 1 
                and self.isBalanced(root.left) 
                and self.isBalanced(root.right))

    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        right = self.maxDepth(root.right) + 1
        left = self.maxDepth(root.left) + 1

        return max(right, left)