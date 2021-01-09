# https://leetcode.com/problems/max-consecutive-ones/

# https://leetcode.com/submissions/detail/440506938/
# 01/08/2021 18:41  

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr = 0
        for n in nums:
            if n == 1:
                curr += 1
                best = max(best, curr)
            else:
                curr = 0
        return best
