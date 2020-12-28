# https://leetcode.com/problems/n-th-tribonacci-number/

# https://leetcode.com/submissions/detail/275278119/
# 11/02/2019 02:42  

class Solution:
    cache = {}
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1
        if self.cache.get(n):
            return self.cache[n]
        else:
            result = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            self.cache[n] = result
            return result