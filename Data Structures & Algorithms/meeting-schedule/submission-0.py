"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: (x.start, x.end))

        prev_end  = intervals[0].end
        for inter in intervals[1:]:
            if inter.start < prev_end:
                return False

            prev_end = inter.end

        return True