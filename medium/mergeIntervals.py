# https://leetcode.com/problems/merge-intervals/

# https://leetcode.com/submissions/detail/435939575/
# 12/29/2020 02:14  

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # loop through intervals
        # if no start point set already, take the next starting merge point
        # save current end point
        # at each interval check if new start point overlaps with previous end point
          # if so, merge
          # else, reset starting merge point
        intervals.sort()
        result = []
        curr = []
        for start, stop in intervals:
            if not curr:
                curr = [start, stop]
            if start < curr[0] and stop >= curr[0]:
                curr[0] = start
                curr[1] = max(curr[1], stop)
            elif start <= curr[1] and stop >= curr[0]:
                curr[1] = max(curr[1], stop)
            else:
                result.append(curr)
                curr = [start, stop]
            # elif prev:
            #     if prev >= start or start < curr[0]:
            #         curr[1] = stop
            #     else:
            #         result.append(curr)
            #         curr = [start, stop]
            # prev = curr[1]
        if curr:
            result.append(curr)
        return result
                