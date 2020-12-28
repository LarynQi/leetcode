# https://leetcode.com/problems/merge-two-binary-trees/

# https://leetcode.com/submissions/detail/284985434/
# 12/10/2019 00:04  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is not None or t2 is not None:
            if t1 is None:
                return t2
            elif t2 is None:
                return t1
            merge = TreeNode(t1.val + t2.val) 
            merge.left = self.mergeTrees(t1.left, t2.left)
            merge.right = self.mergeTrees(t1.right, t2.right)
            return merge