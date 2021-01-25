# https://leetcode.com/problems/minimum-knight-moves/

# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MTUwNzg5OA==

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Approach 1: Tree Recursion
          # Try all possible and valid moves
          # Base cases:
            # 1. Out of range
            # 2. Reached target coordinate
          # Recursive Case:
            # 8 recursive calls, return min of all 8 calls
        # Runtime Analysis:
            # O()
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        start_x = x
        start_y = y
        def helper(x, y):
            if x < 0 or y < 0 or x > start_x or y > start_y:
                return float("inf")
            if x == 0 and y == 0:
                return 0
            return 1 + min([helper(x + m[0], y + m[1]) for m in moves])
        return helper(x, y)

### Solution ###