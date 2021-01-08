# https://leetcode.com/problems/palindrome-linked-list/

# https://leetcode.com/submissions/detail/440250411/
# 01/08/2021 03:28  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        tail = head
        prev = None
        while tail.next is not None:
            tail.prev = prev
            prev = tail
            tail = tail.next
        tail.prev = prev
        while head is not tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.prev
        return True