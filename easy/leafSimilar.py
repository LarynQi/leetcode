# https://leetcode.com/problems/leaf-similar-trees/

# https://leetcode.com/submissions/detail/288756639/
# 12/26/2019 11:24  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def gather(t, leafs):
            if t.left is None and t.right is None:
                leafs += [t.val]
            else:
                if t.left:
                    gather(t.left, leafs)
                if t.right:
                    gather(t.right, leafs)
        l1 = []
        gather(root1, l1)
        l2 = []
        gather(root2, l2)
        if len(l1) != len(l2):
            return False
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True