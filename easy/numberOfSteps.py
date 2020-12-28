# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# https://leetcode.com/submissions/detail/326007952/
# 04/16/2020 23:19  

class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        if num % 2 == 0:
            return 1 + self.numberOfSteps(num / 2)
        return 1 + self.numberOfSteps(num - 1)