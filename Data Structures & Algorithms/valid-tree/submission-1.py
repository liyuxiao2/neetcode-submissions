class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for i in range(n)]
        

        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)
        
        print(adj)

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for e in adj[node]:
                if e == parent:
                    continue
                if not dfs(e, node):
                    return False
            return True


        return dfs(0, -1) and len(visited) == n
        
        