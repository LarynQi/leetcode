# https://leetcode.com/problems/invert-binary-tree/

# https://leetcode.com/submissions/detail/284988835/
# 12/10/2019 00:26

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root