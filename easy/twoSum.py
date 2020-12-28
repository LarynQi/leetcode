# https://leetcode.com/problems/two-sum/

# https://leetcode.com/submissions/detail/435338568/
# 12/27/2020 16:16

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        indices = {}
        for i in range(len(nums)):
            curr = nums[i]
            if target - curr in seen:
                return [indices[target - curr], i]
            seen.add(curr)
            indices[curr] = i

# https://leetcode.com/submissions/detail/268603383/
# 10/10/2019 01:51
# Naive

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]