# https://leetcode.com/problems/delete-node-in-a-linked-list/

# https://leetcode.com/submissions/detail/275943854/
# 11/04/2019 09:50

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next is not None:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
                break
            node = node.next
            