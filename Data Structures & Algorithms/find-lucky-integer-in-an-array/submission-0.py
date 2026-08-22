class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen = defaultdict(int)

        #O(N)
        for n in arr:
            seen[n] += 1
        
        cur_max, cnt = -1, -1

        #(WC O(N))
        for key, count in seen.items():
            if key > cur_max and count == key:
                cur_max, cnt = key, count
        return cur_max
