# https://leetcode.com/problems/power-of-two/

# https://leetcode.com/submissions/detail/440235136/
# 01/08/2021 02:16    

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n & (n - 1)) == 0 and n != 0