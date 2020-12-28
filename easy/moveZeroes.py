# https://leetcode.com/problems/move-zeroes/

# https://leetcode.com/submissions/detail/275568922/
# 11/03/2019 01:57  

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i - count] == 0:
                nums.pop(i - count)
                nums.insert(len(nums), 0)
                count += 1