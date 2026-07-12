class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            cur_interval = res[-1]
            cur_end = cur_interval[1]

            if start <= cur_end:
                cur_interval[1] = max(end, cur_interval[1])
            else:
                res.append([start, end])
        
        return res
                