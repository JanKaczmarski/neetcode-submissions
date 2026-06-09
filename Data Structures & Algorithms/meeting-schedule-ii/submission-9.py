"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for inter in intervals:
            heapq.heappush(start, inter.start)
            heapq.heappush(end, inter.end)

        res = 0
        cnt = 0
        while len(start) > 0:
            if start[0] < end[0]:
                cnt += 1
                heapq.heappop(start)
            else:
                res = max(res, cnt)
                cnt -= 1
                heapq.heappop(end)

        res = max(res, cnt)

        return res