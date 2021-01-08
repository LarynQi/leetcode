# https://leetcode.com/problems/kth-largest-element-in-an-array/

# https://leetcode.com/submissions/detail/440208102/
# 01/08/2021 00:37  

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]