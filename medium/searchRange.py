# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# https://leetcode.com/submissions/detail/291865698/
# 01/06/2020 16:02

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if target in nums:
            first = nums.index(target)
            result[0] = first
            for i in range(first, len(nums)):
                if i == len(nums) - 1 or nums[i + 1] != target:
                    result[1] = i
                    break
        return result