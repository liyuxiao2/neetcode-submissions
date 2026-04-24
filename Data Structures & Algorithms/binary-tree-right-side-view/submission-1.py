# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])

        while q:
            level = len(q)
            temp = []

            for i in range(level):
                v = q.popleft()
                temp.append(v.val)

                if(v.left):
                    q.append(v.left)
                if(v.right):
                    q.append(v.right)
            res.append(temp[-1])
        return res
