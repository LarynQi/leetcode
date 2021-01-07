# https://leetcode.com/problems/search-insert-position/

# https://leetcode.com/submissions/detail/439619659/
# 01/06/2021 19:19  

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        curr = nums[0]
        i = 0
        n = len(nums)
        while curr < target and i < n:
            i += 1
            if i < n:
                curr = nums[i]
        return i