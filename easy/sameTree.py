# https://leetcode.com/problems/same-tree/

# https://leetcode.com/submissions/detail/428276864/
# 12/07/2020 11:36

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        ### Inorder ###
        if not p and not q: return True
        if not p or not q: return False
        
        stack = []
        while True:
            if p or q:
                if not p or not q:
                    return False
                stack.append((p, q))
                p, q = p.left, q.left
            elif stack:
                p, q = stack.pop()
                if not p and not q:
                    continue
                elif not p or not q:
                    return False
                elif p.val != q.val:
                    return False
                p, q = p.right, q.right
            else:
                break
        return True
        
        ### Preorder ###
        # stack = [(p, q)]
        # while stack:
        #     p, q = stack.pop()
        #     if not p and not q:
        #         continue
        #     elif not p or not q:
        #         return False
        #     elif p.val != q.val:
        #         return False
        #     stack.append((p.right, q.right))
        #     stack.append((p.left, q.left))
        # return True
        
        ### Tree Recursion ###
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)