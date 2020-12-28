# https://leetcode.com/problems/contains-duplicate/

# https://leetcode.com/submissions/detail/275950004/
# 11/04/2019 10:18

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for x in nums:
            if x in cache:
                return True
            cache[x] = True
        return False