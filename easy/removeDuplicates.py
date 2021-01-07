# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# https://leetcode.com/submissions/detail/439617944/
# 01/06/2021 19:14  

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        i = 0
        while i < len(nums):
            curr = nums[i]
            if prev is not None:
                if prev == curr:
                    nums.pop(i)
                    # nums.remove(curr)
                else:
                    prev = curr
                    i += 1
            else:
                prev = curr
                i += 1
        return len(nums)
                    
        ### Bad time and space complexity ###
        # count = 0
        # seen = set()
        # i = 0
        # while i < len(nums):
        #     curr = nums[i]
        #     if curr in seen:
        #         nums.pop(i)
        #     else:
        #         seen.add(curr)
        #         i += 1
        # return len(nums)
            