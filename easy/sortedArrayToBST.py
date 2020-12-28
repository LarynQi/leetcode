# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# https://leetcode.com/submissions/detail/275976887/
# 11/04/2019 12:11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            mid = len(nums) // 2
            bst = TreeNode(nums[mid])
            bst.left = self.sortedArrayToBST(nums[0:mid])
            bst.right = self.sortedArrayToBST(nums[mid + 1:])
            return bst