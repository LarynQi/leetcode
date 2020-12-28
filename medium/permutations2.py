# https://leetcode.com/problems/permutations-ii/

# https://leetcode.com/submissions/detail/433898279/
# 12/23/2020 17:16

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        result = []
        seen = set()
        for i in range(len(nums)):
            subresult = []
            for p in self.permuteUnique(nums[:i] + nums[i + 1:]):
                curr = [nums[i]] + p
                if str(curr) not in seen:
                    subresult.append(curr)
                    seen.add(str(curr))
            result += subresult 
        return result