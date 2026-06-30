import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            v = heapq.heappop(gifts)
            new_v = math.isqrt(abs(v))

            heapq.heappush(gifts, -new_v)
        
        return abs(sum(gifts))