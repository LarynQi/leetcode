# https://leetcode.com/problems/complement-of-base-10-integer/
# same as https://leetcode.com/problems/number-complement/

# https://leetcode.com/submissions/detail/440527291/
# 01/08/2021 19:53  

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        num = N
        count = len(str(bin(num))) - 2
        ans = str(bin(((2 ** 32) - 1) ^ num))[2:]
        return int(ans[len(ans) - count:], 2)