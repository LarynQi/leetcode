# https://leetcode.com/problems/remove-linked-list-elements/

# https://leetcode.com/submissions/detail/275948494/
# 11/04/2019 10:12

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        lst = head
        prev = head
        if not head:
            return head
        while head is not None and head.val == val:
            lst = head.next
            head = head.next
        while head is not None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
                
           
        return lst