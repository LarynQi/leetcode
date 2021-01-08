# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# https://leetcode.com/submissions/detail/439981200/
# 01/07/2021 14:03  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()
        queue = [root]
        while queue:
            curr = queue.pop()
            if not curr:
                continue
            elif k - curr.val in seen:
                return True
            seen.add(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        return False