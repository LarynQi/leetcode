# https://leetcode.com/problems/guess-number-higher-or-lower/

# https://leetcode.com/submissions/detail/291896596/
# 01/06/2020 18:12  

# # The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        mid = n // 2 
        while mid:
            g = guess(mid)
            if g == 0:
                return mid
            if g == 1:
                if (n + mid) % 2 == 1:
                    mid = (n + mid) // 2 + 1
                else:
                    mid = (n + mid) // 2
            else:
                n = mid
                mid = mid // 2