"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) == 0: return True

        intervals.sort(key = lambda x:x.start)

        ans = list()
        ans.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i].start >= ans[-1].end: ans.append(intervals[i])
            else: return False

        return True
