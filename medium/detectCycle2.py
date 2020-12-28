# https://leetcode.com/problems/linked-list-cycle-ii/

# https://leetcode.com/submissions/detail/291879042/
# 01/06/2020 17:03

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cache = {}
        while head is not None:
            if head in cache:
                return head
            cache[head] = True
            head = head.next