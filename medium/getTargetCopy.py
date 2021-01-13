# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# https://leetcode.com/submissions/detail/442290157/
# 01/12/2021 19:28  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [original]
        vals = []
        while stack:
            curr = stack.pop()
            if curr:
                vals.append(curr.val)
                if curr is target:
                    break
                stack.append(curr.left)
                stack.append(curr.right)
        stack = [cloned]
        vals_clone = []
        while stack:
            curr = stack.pop()
            if curr:
                vals_clone.append(curr.val)
                if curr.val == target.val and vals == vals_clone:
                    return curr
                stack.append(curr.left)
                stack.append(curr.right)