# https://leetcode.com/problems/maximum-binary-tree/

# https://leetcode.com/submissions/detail/288119421/
# 12/23/2019 18:00  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        curr = TreeNode(max(nums))
        index = nums.index(curr.val)
        if index < len(nums) - 1:  
            curr.right = self.constructMaximumBinaryTree(nums[index + 1:])
        curr.left = self.constructMaximumBinaryTree(nums[:index]) 
        return curr