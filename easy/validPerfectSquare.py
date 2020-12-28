# https://leetcode.com/problems/valid-perfect-square/

# https://leetcode.com/submissions/detail/291874871/
# 01/06/2020 16:44  

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        base = 1
        while base * base <= num:
            if base * base == num:
                return True
            base += 1
        return False