class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        min_h = [(0, k)]
        visited = set()
        t = 0

        while min_h:
            weight, node = heapq.heappop(min_h)

            if node in visited:
                continue
            
            visited.add(node)
            t = max(t, weight)

            for edge, w2 in edges[node]:
                if edge not in visited:
                    heapq.heappush(min_h, (weight + w2, edge))
        
        return t if len(visited) == n else -1

