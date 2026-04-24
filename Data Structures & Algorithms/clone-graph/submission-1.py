"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        res = {}
        res[node] = Node(node.val)

        q = deque([node])

        while q:
            cur = q.popleft()

            for n in cur.neighbors:
                if n not in res: #adds new node to the result
                    res[n] = Node(n.val)
                    q.append(n)
                
                res[cur].neighbors.append(res[n]) #adds that neighbor node onto our currnet
        
        return res[node]