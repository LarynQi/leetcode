# https://leetcode.com/problems/reverse-integer/

# https://leetcode.com/submissions/detail/268608154/
# 10/10/2019 02:27

class Solution:
    def reverse(self, x: int) -> int:
        new = 0
        new_neg = 0
        neg = False
        while abs(x) > 0:
            if x > 0 and not neg:
                new = new * 10 + x % 10
            elif neg:
                new_neg = new_neg * 10 + x % 10
            else:
                new_neg = new_neg * 10 + -(x % -10)
                neg = True
                x = -x
            x //= 10
        if abs(new) >= 2 ** 31 or abs(new_neg) >= 2 ** 31:
            return 0
        if not neg:
            return new
        return -new_neg