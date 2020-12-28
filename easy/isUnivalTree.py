# https://leetcode.com/problems/univalued-binary-tree/

# https://leetcode.com/submissions/detail/284992030/
# 12/10/2019 00:46  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is not None:
            if root.right is not None:
                if root.left.val != root.right.val:
                    return False
            if root.val != root.left.val:
                return False
        if root.right is not None:
            if root.val != root.right.val:
                return False
        return False not in [self.isUnivalTree(root.left), self.isUnivalTree(root.right)]