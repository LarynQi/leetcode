# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# https://leetcode.com/submissions/detail/292001490/
# 01/07/2020 00:36  

# class Solution:
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