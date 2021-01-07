# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# https://leetcode.com/submissions/detail/439625034/
# 01/06/2021 19:33  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        original = head
        prev = None
        while head is not None:
            if prev:
                if prev.val == head.val:
                    prev.next = head.next
                else:
                    prev = head
            else:
                prev = head
            head = head.next
        return original