from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cur = set()
        queue = deque()

        for num in nums:
            if not (len(cur) < k + 1):
                val = queue.popleft()
                cur.remove(val)

            if num in cur:
                return True
            
            #we do this no matter what
            cur.add(num)
            queue.append(num)
        return False
            