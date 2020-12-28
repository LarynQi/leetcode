# https://leetcode.com/problems/find-the-duplicate-number/

# https://leetcode.com/submissions/detail/291876245/
# 01/06/2020 16:50  

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cache = {}
        for n in nums:
            if n in cache:
                return n
            cache[n] = 1