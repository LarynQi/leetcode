# https://leetcode.com/problems/symmetric-tree/

# https://leetcode.com/submissions/detail/435391481/
# 12/27/2020 19:11  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.iterative(root)
        ### Recursive ###
        def helper(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        return helper(root, root)
    
    ### Iterative ###
    def iterative(self, root):
        q = []
        q.append(root)
        q.append(root)
        while q:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True