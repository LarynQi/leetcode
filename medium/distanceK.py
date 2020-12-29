# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# https://leetcode.com/submissions/detail/435398485/
# 12/27/2020 19:33  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def get_parents(node, parent=None):
            if node:
                node.parent = parent
                get_parents(node.left, node)
                get_parents(node.right, node)
        get_parents(root)
        q = [[target, 0]]
        seen = set()
        seen.add(target)
        while q:
            if q[0][1] == K:
                return [n.val for n, distance in q]
            curr, distance = q.pop(0)
            for n in (curr.left, curr.right, curr.parent):
                if n and n not in seen:
                    seen.add(n)
                    q.append([n, distance + 1])
        return []
