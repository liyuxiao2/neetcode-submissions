class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        res = nums[:]

        min_h = [(num, i) for i, num in enumerate(nums)]

        heapq.heapify(min_h)

        for i in range(k):
            num, i = heapq.heappop(min_h)
            res[i] *= multiplier

            heapq.heappush(min_h, (res[i], i))
        
        return res