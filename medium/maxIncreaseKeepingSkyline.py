# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

# https://leetcode.com/submissions/detail/268833962/
# 10/10/2019 21:28  
# Wrong Answer

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skyline_tb = []
        skyline_lr = []
        for i in range(len(grid[0])):
            max = grid[0][i]
            for j in grid:
                if j[i] > max:
                    max = j[i]
                skyline_tb += [max]
        print(skyline_tb)
        for i in grid:
            max = 0
            for j in i:
                if j > max:
                    max = j
            skyline_lr += [max]