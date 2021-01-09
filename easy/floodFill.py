# https://leetcode.com/problems/flood-fill/

# https://leetcode.com/submissions/detail/440512300/
# 01/08/2021 19:01  

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = [(sr, sc)]
        original = image[sr][sc]
        rows = len(image)
        seen = set()
        while stack:
            i, j = stack.pop()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if i >= rows or i < 0:
                continue
            cols = len(image[i])
            if j >= cols or j < 0:
                continue
            if image[i][j] == original:
                image[i][j] = newColor
                stack.append((i - 1, j))
                stack.append((i + 1, j))
                stack.append((i, j - 1))
                stack.append((i, j + 1))
        return image