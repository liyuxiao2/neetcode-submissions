class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        candidate = []
        adj = [[] for _ in range(len(edges) + 1)]
        
        def dfs(node, edge, par):
            if node == edge:
                return True
            
            seen.add(node)

            for e in adj[node]:
                if e not in seen:
                    if dfs(e, edge, seen):
                        return True
            return False
        

        for node, edge in edges:
            seen = set()

            if dfs(node, edge, seen):
                return [node, edge]
            
            adj[node].append(edge)
            adj[edge].append(node)
        return []


                

