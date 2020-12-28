# https://leetcode.com/problems/minimum-path-sum

# https://leetcode.com/submissions/detail/292023647/
# 01/07/2020 03:12  
# Time Limit Exceeded

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def helper(grid, pos):
            if pos == [rows - 1, cols - 1]:
                return grid[pos[0]][pos[1]]
            if pos[1] == cols - 1:
                return grid[pos[0]][pos[1]] + helper(grid, [pos[0] + 1, pos[1]])
            elif pos[0] == rows - 1:
                return grid[pos[0]][pos[1]] + helper(grid, [pos[0], pos[1] + 1])
            rightPath = grid[pos[0]][pos[1]] + helper(grid, [pos[0], pos[1] + 1])
            downPath = grid[pos[0]][pos[1]] + helper(grid, [pos[0] + 1, pos[1]])
            return min(rightPath, downPath)
        return helper(grid, [0, 0])