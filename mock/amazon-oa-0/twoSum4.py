# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MTQ0NjM4OA==

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ### Array search: ###
        # loop through all elements in BST
          # if the complement of the current element exists in `seen`, return true
          # else, add current element to seen
        seen = set()
        def helper(root, k, seen):
            if not root:
                return False
            elif k - root.val in seen:
                return True
            seen.add(root.val)
            return helper(root.left, k, seen) or helper(root.right, k, seen)
        return helper(root, k, seen)