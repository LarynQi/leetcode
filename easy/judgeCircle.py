# https://leetcode.com/problems/robot-return-to-origin/

# https://leetcode.com/submissions/detail/288639701/
# 12/25/2019 22:48  

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            if move == "U":
                y += 1
            if move == "D":
                y -= 1
            if move == "R":
                x += 1
            if move == "L":
                x -= 1
        return x == 0 and y == 0