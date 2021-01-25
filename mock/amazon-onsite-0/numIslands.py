# https://leetcode.com/problems/number-of-islands/

# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MTUwNTI4Ng==

class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        
        count = 0
        for x in range(m):
            for y in range(n):
                if (x, y) not in seen and grid[x][y] == "1":
                    count += 1
                    queue = [(x, y)]
                    while queue:
                        i, j = queue.pop()
                        if i >= 0 and i < m and j >= 0 and j < n and (i, j) not in seen:
                            if grid[i][j] == "1":
                                seen.add((i, j))
                                queue.append((i + 1, j))
                                queue.append((i - 1, j))
                                queue.append((i, j + 1))
                                queue.append((i, j - 1))
        return count