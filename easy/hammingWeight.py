# https://leetcode.com/problems/number-of-1-bits/

# https://leetcode.com/submissions/detail/440236304/
# 01/08/2021 02:21  

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count