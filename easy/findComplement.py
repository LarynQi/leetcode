# https://leetcode.com/problems/number-complement/
# same as https://leetcode.com/problems/complement-of-base-10-integer/

# https://leetcode.com/submissions/detail/440508275/
# 01/08/2021 18:46  

class Solution:
    def findComplement(self, num: int) -> int:
        count = len(str(bin(num))) - 2
        ans = str(bin(((2 ** 32) - 1) ^ num))[2:]
        return int(ans[len(ans) - count:], 2)