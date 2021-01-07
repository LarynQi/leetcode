# https://leetcode.com/problems/powx-n/

# https://leetcode.com/submissions/detail/439778277/
# 01/07/2021 03:18  

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        count = 0
        int_n = abs(n)
        while int_n > 1:
            int_n >>= 1
            count += 1
        mask = 1 << count
        int_n = abs(n)
        result = 1
        while count > -1:
            curr = int_n & mask
            result *= result
            if curr != 0:
                result *= x
            mask >>= 1
            count -= 1
        if n < 0:
            return 1 / result
        return result
        # if n == 0:
        #     return 1
        # count = 0
        # temp = 1
        # int_n = abs(int(n))
        # while int_n > 1:
        #     int_n >>= 1
        #     count += 1
        #     temp *= 2
        # result = x
        # for i in range(count):
        #     result *= result
        # for i in range(temp, abs(n)):
        #     result *= x
        # if n < 0:
        #     return 1 / result
        # return result