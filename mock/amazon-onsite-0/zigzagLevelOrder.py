# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# https://leetcode.com/interview/reports/SW50ZXJ2aWV3U2Vzc2lvbk5vZGU6MTUwNTI4Ng==

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS except invert order after every level by appending boolean value to each element in the queue
        queue = [(root, 0)]
        result = []
        while queue:
            node, level = queue.pop()
            if node:
                if len(result) <= level:
                    result.append([])
                if level % 2 == 1:
                    result[level] = [node.val] + result[level]
                else:
                    result[level].append(node.val)
                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))
        return result
