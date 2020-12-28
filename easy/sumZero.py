# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

# https://leetcode.com/submissions/detail/291882451/
# 01/06/2020 17:17  

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result += [0]
        for i in range(1, n // 2 + 1):
            result += [-i, i]
        return result