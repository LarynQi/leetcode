# https://leetcode.com/problems/merge-two-sorted-lists/

# https://leetcode.com/submissions/detail/284982810/
# 12/09/2019 23:49

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            link = ListNode(l1.val)
            link.next = self.mergeTwoLists(l1.next, l2)
            return link
        else:
            link = ListNode(l2.val)
            link.next = self.mergeTwoLists(l1, l2.next)
            return link