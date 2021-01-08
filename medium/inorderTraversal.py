# https://leetcode.com/problems/binary-tree-inorder-traversal/

# https://leetcode.com/submissions/detail/439999936/
# 01/07/2021 15:02  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        stack = []
        curr = root
        while curr is not None:
            stack.append((curr, False))
            curr = curr.left
        result = []
        while stack:
            curr, visit = stack.pop()
            if curr:
                if not visit:
                    result.append(curr.val)
                    stack.append((curr.right, True))
                if visit:
                    result.extend(self.inorderTraversal(curr))
        return result
                
                