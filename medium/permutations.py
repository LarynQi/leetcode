# https://leetcode.com/problems/permutations/

# https://leetcode.com/submissions/detail/433891372/
# 12/23/2020 16:48

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            result += [[nums[i]] + p for p in Solution.permute(self, nums[:i] + nums[i + 1:])]
        return result
