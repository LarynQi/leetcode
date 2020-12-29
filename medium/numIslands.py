# https://leetcode.com/problems/number-of-islands/

# https://leetcode.com/submissions/detail/435765830/
# 12/28/2020 16:50  


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        import collections
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "0"
                    q = collections.deque([[i, j]])
                    while q:
                        row, col = q.popleft()
                        if row > 0 and grid[row - 1][col] == "1":
                            grid[row - 1][col] = "0"
                            q.append([row - 1, col])
                        if row < len(grid) - 1 and grid[row + 1][col] == "1":
                            grid[row + 1][col] = "0"
                            q.append([row + 1, col])
                        if col > 0 and grid[row][col - 1] == "1":
                            grid[row][col - 1] = "0"
                            q.append([row, col - 1])
                        if col < len(grid[i]) - 1 and grid[row][col + 1] == "1":
                            grid[row][col + 1] = "0"
                            q.append([row, col + 1])
        return count
                    
                    
        # count = 0
        # islands = {}
        # island_id = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         counted = False
        #         if grid[i][j] == "1":
        #             if i == 0 or grid[i - 1][j] == "0" or (grid[i - 1][j] == "1" and (i - 1, j) in islands and not islands[i - 1, j][1]):
        #                 if i == len(grid) - 1 or grid[i + 1][j] == "0" or (grid[i + 1][j] == "1" and (i + 1, j) in islands and not islands[i + 1, j][1]):
        #                     if j == 0 or grid[i][j - 1] == "0" or (grid[i][j - 1] == "1" and (i, j - 1) in islands and not islands[i, j - 1][1]):
        #                         if j == len(grid[i]) - 1 or grid[i][j + 1] == "0" or (grid[i][j + 1] == "1" and (i, j + 1) in islands and not islands[i, j + 1][1]):
        #                             count += 1
        #                             print(i, j)
        #                             print(islands)
        #                             counted = True
        #             alone = True
        #             updated = False
        #             if i != 0 and grid[i - 1][j] == "1":
        #                 alone = False
        #                 curr = (i - 1, j)
        #                 if curr in islands:
        #                     if counted:
        #                         islands[i - 1, j][1] = counted
        #                     islands[i, j] = islands[i - 1, j]
        #                     updated = True
        #             if i != len(grid) - 1 and grid[i + 1][j] == "1":
        #                 alone = False
        #                 curr = (i + 1, j)
        #                 if curr in islands:
        #                     if counted:
        #                         islands[i + 1, j][1] = counted
        #                     islands[i, j] = islands[i + 1, j]
        #                     updated = True
        #             if j != 0 and grid[i][j - 1] == "1":
        #                 alone = False
        #                 curr = (i, j - 1)
        #                 if curr in islands:
        #                     if counted:
        #                         islands[i, j - 1][1] = counted
        #                     islands[i, j] = islands[i, j - 1]
        #                     updated = True
        #             if j != len(grid[i]) - 1 and grid[i][j + 1] == "1":
        #                 alone = False
        #                 curr = (i, j + 1)
        #                 if curr in islands:
        #                     if counted:
        #                         islands[i, j + 1][1] = counted
        #                     islands[i, j] = islands[i - 1, j + 1]
        #                     updated = True
        #             if not alone and (i, j) not in islands:
        #                 islands[i, j] = [island_id, counted]
        #                 island_id += 1
        #             if not alone:
        #                 for il in islands:
        #                     if islands[il][0] == islands[i, j][0] and counted:
        #                         islands[il][1] = counted
        #                     if updated and (il[0] in (i - 1, i + 1) or il[1] in (j - 1, j + 1)):
        #                         islands[il][0] = islands[i, j][0]
        # return count