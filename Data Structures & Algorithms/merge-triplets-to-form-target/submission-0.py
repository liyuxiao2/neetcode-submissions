class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur_t = [0] * 3

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            cur_t = [max(cur_t[0], t[0]), max(cur_t[1], t[1]), max(cur_t[2], t[2])]

            if cur_t == target:
                return True
        
        return cur_t == target