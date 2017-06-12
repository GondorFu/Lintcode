

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x:(x.start, x.end))
        rlt = [intervals[0]]
        for v in intervals:
            if rlt[-1].end < v.start:
                rlt.append(v)
            else:
                rlt[-1].end = max(rlt[-1].end, v.end)
        return rlt
        