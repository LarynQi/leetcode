# https://leetcode.com/problems/running-sum-of-1d-array/

# https://leetcode.com/submissions/detail/439766977/
# 01/07/2021 02:29  

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for n in nums:
            total += n
            result.append(total)
        return result