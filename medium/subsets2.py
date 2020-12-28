# https://leetcode.com/problems/subsets-ii/

# https://leetcode.com/submissions/detail/428282241/
# 12/07/2020 11:56  
# Wrong Answer

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, sofar):
            if not nums:
                return sofar
            ret = helper(nums[1:], [s + [nums[0]] if s + [nums[0]] not in sofar else s for s in sofar])
            i = len(ret)
            ret.extend(helper(nums[1:], sofar))
            return ret[:i] + list(filter(lambda x: x not in ret[:i], ret[i:]))
            
        return helper(nums, [[]])