# https://leetcode.com/problems/matrix-diagonal-sum/

# https://leetcode.com/submissions/detail/441050589/
# 01/09/2021 23:31  

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(n):
            # print(total)
            total += mat[i][i]
            if not (n % 2 == 1 and i == n // 2):
                total += mat[i][n - i - 1]
        return total