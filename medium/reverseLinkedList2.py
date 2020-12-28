# https://leetcode.com/problems/reverse-linked-list-ii/

# https://leetcode.com/submissions/detail/284233317/
# 12/06/2019 18:02  
# Memory Limit Exceeded

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = head
        pointer = head
        if m == n:
            return head
        while m > 0:
            prev = pointer
            pointer = pointer.next
            n -= 1
            m -= 1
        end = prev
        while n > 0:
            next_node = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = next_node
            n -= 1
        if next_node is not None:
            end.next = pointer
            head.next = prev
        return head