# https://leetcode.com/problems/remove-element/

# https://leetcode.com/submissions/detail/268612914/
# 10/10/2019 03:10

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        original = len(nums)
        for i in nums:
            if i == val:
                length -= 1
        k = 0
        while k < original - length:
            nums.remove(val)
            k += 1
        return length