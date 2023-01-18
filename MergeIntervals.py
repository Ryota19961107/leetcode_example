from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        intervals.append([-1, -1])
        i = 1
        while intervals[i] != [-1, -1]: 
            cur = intervals[i]
            prev = intervals[i - 1]
            if cur[0] <= prev[1]:
                intervals[i] = [min(prev[0], cur[0]), max(prev[1], cur[1])]
                del intervals[i - 1]
                i -= 1
            i += 1
        return intervals[:len(intervals) - 1]