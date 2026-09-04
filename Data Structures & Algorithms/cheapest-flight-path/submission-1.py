class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # djkstra's algo
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 2) for _ in range(n)]

        for n, e, w in flights:
            adj[n].append([e, w])
        
        dist[src][0] = 0
        heap = [(0, src, -1)] #cost, node, step


        while len(heap):
            cst, n, step = heapq.heappop(heap)

            
            if dst == n: return cst
            if step == k or dist[n][step + 1] < cst:
                continue
            
            for e, w in adj[n]:
                nextCst = cst + w
                nextStep = 1 + step
                if dist[e][nextStep + 1] > nextCst:
                    dist[e][nextStep + 1] = nextCst
                heapq.heappush(heap, (nextCst, e, nextStep))
        
        return -1
        
      


