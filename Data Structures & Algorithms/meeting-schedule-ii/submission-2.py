"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=self.by_start)
        
        min_h  = []

        for interval in intervals:
            if min_h and min_h[0] <= interval.start:
                heapq.heappop(min_h)
            heapq.heappush(min_h, interval.end)
        
        return len(min_h)

    def by_start(self, e):
        return e.start
    