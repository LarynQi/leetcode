# https://leetcode.com/problems/deepest-leaves-sum/

# https://leetcode.com/submissions/detail/442316389/
# 01/12/2021 20:38  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = deque([(root, 1)])
        levels = {}
        max_lvl = 0
        while queue:
            curr, level = queue.pop()
            if curr:
                max_lvl = max(level, max_lvl)
                levels[level] = levels.get(level, 0) + curr.val
                queue.appendleft((curr.left, level + 1))
                queue.appendleft((curr.right, level + 1))
        return levels[max_lvl]
                