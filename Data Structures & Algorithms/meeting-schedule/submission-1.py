"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=self.by_start)
        res = intervals[0]

        for interval in intervals[1:]:
            if interval.start < res.end:
                return False
            else:
                res = interval
        
        return True

    def by_start(self, e):
        return e.start

        