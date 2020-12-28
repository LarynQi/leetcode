# https://leetcode.com/problems/minimum-time-visiting-all-points/

# https://leetcode.com/submissions/detail/288191477/
# 12/24/2019 00:03  

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            x1 = points[i - 1][0]
            y1 = points[i - 1][1]
            x2 = points[i][0]
            y2 = points[i][1]
            diffx = abs(x2 - x1)
            diffy = abs(y2 - y1)
            time += min(diffx, diffy)
            time += abs(diffy - diffx)
        return time