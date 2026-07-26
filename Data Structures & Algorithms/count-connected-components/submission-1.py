class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0

        adj = [[] for _ in range(n)]

        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)
        

        visited = set()
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)

            for e in adj[node]:
                dfs(e)
        

        for i in edges:
            if i[0] in visited:
                continue
            else:
                count += 1
                dfs(i[0])
        
        return (count + (n - len(visited)))