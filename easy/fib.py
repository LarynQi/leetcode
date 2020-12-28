# https://leetcode.com/problems/fibonacci-number/

# https://leetcode.com/submissions/detail/269142125/
# 10/12/2019 01:53  

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)