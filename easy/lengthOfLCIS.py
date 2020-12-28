# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

# https://leetcode.com/submissions/detail/291891941/
# 01/06/2020 17:55  

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # m = 0
        # while len(nums) > m:
        #     i = 1
        #     while i < len(nums) and nums[i] > nums[i - 1]:
        #         i += 1
        #     m = max(i, m)
        #     nums = nums[i:]
        # return m
        start = 0
        m = 0
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                start = i
            m = max(m, i - start + 1)
        return m