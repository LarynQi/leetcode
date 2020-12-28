# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# https://leetcode.com/submissions/detail/284991039/
# 12/10/2019 00:40

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))