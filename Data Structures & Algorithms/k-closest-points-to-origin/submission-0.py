class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we can calculate the euclidian distance for each pair

        #add them to a heap

        #pop out first one if it exceeds k

        res = []
        for x, y in points:
            dist = (math.sqrt((0 - x)**2 + (0 - y)**2))
            res.append([dist, x, y])
        
        heapq.heapify(res)
        final = []
        while(k > 0):
            dist, x, y = heapq.heappop(res)
            final.append([x, y])
            k -= 1
        

        return final
        
        


