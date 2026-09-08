class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []


        for x, y in points:
            distance = math.sqrt((0 - x) ** 2 + (0 - y) ** 2)

            heapq.heappush(heap, (distance, [x,y]))
        
        print(heap)

        res = []

        for i in range(k):
            _, coord = heapq.heappop(heap)
            res.append(coord)

        return res