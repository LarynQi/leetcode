# https://leetcode.com/problems/single-number/

# https://leetcode.com/submissions/detail/439629864/
# 01/06/2021 19:46  

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor