# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# https://leetcode.com/submissions/detail/433903486/
# 12/23/2020 17:37  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(t, maximum):
            if not t:
                return 0
            if t.val >= maximum:
                return 1 + helper(t.left, max(maximum, t.val)) + helper(t.right, max(maximum, t.val))
            else:
                return helper(t.left, max(maximum, t.val)) + helper(t.right, max(maximum, t.val))
        return helper(root, float("-inf"))