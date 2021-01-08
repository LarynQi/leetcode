# https://leetcode.com/problems/hamming-distance/

# https://leetcode.com/submissions/detail/440245607/
# 01/08/2021 03:04  

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor > 0:
            if xor & 1:
                count += 1
            xor >>= 1
        return count