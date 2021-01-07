# https://leetcode.com/problems/subtree-of-another-tree/

# https://leetcode.com/submissions/detail/439586159/
# 01/06/2021 17:36  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check(s, t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            return s.val == t.val and check(s.left, t.left) and check(s.right, t.right)
        import collections
        queue = collections.deque([])
        queue.append(s)
        while queue:
            curr = queue.popleft()
            if not curr:
                continue
            if check(curr, t):
                return True
            queue.append(curr.left)
            queue.append(curr.right)
        return False