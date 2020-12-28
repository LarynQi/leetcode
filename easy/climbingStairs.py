# https://leetcode.com/problems/climbing-stairs/

# https://leetcode.com/submissions/detail/275278564/
# 11/02/2019 02:48

class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        elif self.cache.get(n):
            return self.cache[n]
        else:
            result = self.climbStairs(n - 1) + self.climbStairs(n-2)
            self.cache[n] = result
            return result