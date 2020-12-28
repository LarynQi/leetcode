# https://leetcode.com/problems/counting-bits/

# https://leetcode.com/submissions/detail/434239305/
# 12/24/2020 16:58  

class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for i in range(num + 1):
            count = 0
            while i > 0:
                count += i & 1
                i >>= 1
            result.append(count)
        return result