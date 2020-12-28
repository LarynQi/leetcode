# https://leetcode.com/problems/maximum-subarray/

# https://leetcode.com/submissions/detail/292143933/
# 01/07/2020 13:34

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # def helper(lst, cont, total):
        #     if len(lst) == 1:
        #         return lst[0]
        #     if not total:
        #         return max(helper(lst[1:], cont, None), helper(lst[1:], True, lst[0]))
        #     if cont:
        #         return max(helper(lst[1:], cont, lst[0] + total), total)
        #     return max(helper(lst[1:], cont, total), helper(lst[1:], True, total + lst[0]))
        # return helper(nums, False, None)
        # if len(nums) == 1:
        #     return nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)