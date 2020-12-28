# https://leetcode.com/problems/single-element-in-a-sorted-array/

# https://leetcode.com/submissions/detail/275876055/
# 11/04/2019 02:04  

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        middle = len(nums) // 2
        if len(nums) == 1:
            return nums[0]
        elif nums[middle] != nums[middle + 1] and nums[middle] != nums[middle - 1]:
            return nums[middle]
        elif middle % 2 == 0:
            if nums[middle] == nums[middle - 1]:
                return self.singleNonDuplicate(nums[0:middle + 1])
            else:
                return self.singleNonDuplicate(nums[middle:]) 
        else:
            if nums[middle] == nums[middle + 1]:
                return self.singleNonDuplicate(nums[0:middle])
            else:
                return self.singleNonDuplicate(nums[middle + 1:])