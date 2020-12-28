# https://leetcode.com/problems/subsets/

# https://leetcode.com/submissions/detail/427930751/
# 12/06/2020 13:13

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, sofar):
            if not nums:
                return sofar
            ret = helper(nums[1:], [s + [nums[0]] if nums[0] not in s else s for s in sofar])
            ret.extend(helper(nums[1:], sofar))
            return ret
            
        return helper(nums, [[]])