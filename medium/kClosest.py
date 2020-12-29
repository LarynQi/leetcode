# https://leetcode.com/problems/k-closest-points-to-origin/

# https://leetcode.com/submissions/detail/436098011/
# 12/29/2020 11:59  
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance(p0):
            return sqrt((p0[0] - 0) ** 2 + (p0[1] - 0) ** 2)
        points.sort(key=distance)
        return points[:K]